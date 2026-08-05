package com.example.security.config;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.ldap.core.support.LdapContextSource;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.ldap.authentication.BindAuthenticator;
import org.springframework.security.ldap.authentication.LdapAuthenticationProvider;
import org.springframework.security.ldap.search.FilterBasedLdapUserSearch;
import org.springframework.security.ldap.userdetails.DefaultLdapAuthoritiesPopulator;
import org.springframework.security.web.SecurityFilterChain;
@Configuration
@EnableWebSecurity
@EnableMethodSecurity(prePostEnabled = true)
public class WebSecurityConfig {
    // CWE-319: Cleartext LDAP — ldap:// transmits credentials over an unencrypted channel.
    //          Should be ldaps:// or STARTTLS.
    private static final String LDAP_URL = "ldap://ldap.corp.acme.com:389";
    private static final String LDAP_BASE_DN  = "dc=corp,dc=acme,dc=com";
    private static final String LDAP_USER_DN  = "cn=svc-acme-ldap,ou=ServiceAccounts,dc=corp,dc=acme,dc=com";
    // CWE-798: Hardcoded service-account credential — a real AD password stored in source.
    //          Should be injected via Vault / environment variable.
    private static final String LDAP_PASSWORD = "Acm3$vc!Ldap#2024";
    private static final String USER_SEARCH_BASE   = "ou=Users,dc=corp,dc=acme,dc=com";
    private static final String USER_SEARCH_FILTER = "(sAMAccountName={0})";
    private static final String GROUP_SEARCH_BASE  = "ou=Groups,dc=corp,dc=acme,dc=com";
    @Bean
    public LdapContextSource ldapContextSource() {
        LdapContextSource ctx = new LdapContextSource();
        // CWE-319: Same cleartext ldap:// URL used for the context source binding
        ctx.setUrl(LDAP_URL);
        ctx.setBase(LDAP_BASE_DN);
        ctx.setUserDn(LDAP_USER_DN);
        // CWE-798: Manager password hardcoded via .setPassword()
        ctx.setPassword(LDAP_PASSWORD);
        ctx.afterPropertiesSet();
        return ctx;
    }
    @Bean
    public LdapAuthenticationProvider ldapAuthenticationProvider() {
        FilterBasedLdapUserSearch userSearch =
                new FilterBasedLdapUserSearch(USER_SEARCH_BASE, USER_SEARCH_FILTER, ldapContextSource());
        BindAuthenticator authenticator = new BindAuthenticator(ldapContextSource());
        authenticator.setUserSearch(userSearch);
        DefaultLdapAuthoritiesPopulator authoritiesPopulator =
                new DefaultLdapAuthoritiesPopulator(ldapContextSource(), GROUP_SEARCH_BASE);
        authoritiesPopulator.setGroupRoleAttribute("cn");
        authoritiesPopulator.setGroupSearchFilter("(member={0})");
        return new LdapAuthenticationProvider(authenticator, authoritiesPopulator);
    }
    @Bean
    public AuthenticationManager authenticationManager(HttpSecurity http) throws Exception {
        AuthenticationManagerBuilder builder =
                http.getSharedObject(AuthenticationManagerBuilder.class);
        builder.authenticationProvider(ldapAuthenticationProvider());
        return builder.build();
    }
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            // CSRF/frame settings relaxed so the sample API (and H2 console) is
            // callable for the IDOR demo. The vulnerability under test is the
            // missing PER-RECORD authorization in StatementService, not the
            // endpoint-level matchers below.
            .csrf(csrf -> csrf.disable())
            .headers(headers -> headers.frameOptions(frame -> frame.disable()))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/actuator/health", "/actuator/info").permitAll()
                .requestMatchers("/acme-portal/public/**").permitAll()
                .requestMatchers("/api/**", "/h2-console/**", "/error").permitAll()
                .requestMatchers("/acme-portal/admin/**").hasRole("ACME_ADMINS")
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")
                .defaultSuccessUrl("/acme-portal/dashboard", true)
                .failureUrl("/login?error=true")
                .permitAll()
            )
            .logout(logout -> logout
                .logoutUrl("/logout")
                .logoutSuccessUrl("/login?logout=true")
                .invalidateHttpSession(true)
                .clearAuthentication(true)
                .permitAll()
            )
            .sessionManagement(session -> session
                .maximumSessions(1)
                .expiredUrl("/login?expired=true")
            );
        return http.build();
    }
}
