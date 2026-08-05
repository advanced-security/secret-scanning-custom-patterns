package com.example.db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Ad-hoc connectivity probe against the SQL Server warehouse.
 *
 * Reachable from {@code GET /api/admin/db-check} so the insecure-connection
 * sink below is not discarded as unreachable.
 */
@RestController
@RequestMapping("/api/admin")
public class DbConnectivityCheck {

    /**
     * VULNERABILITY — CWE-295 (Improper Certificate Validation):
     * {@code trustServerCertificate=true} disables TLS certificate validation
     * on the JDBC connection, so the driver accepts ANY server certificate.
     * Combined with {@code encrypt=true} this gives a false sense of security:
     * the channel is encrypted but unauthenticated, enabling a man-in-the-middle
     * to impersonate the database. Mirrors the JDBC URLs in application-*.yaml.
     */
    private static final String JDBC_URL =
            "jdbc:sqlserver://prod-db01.corp.acme.com:1433;databaseName=AcmePortal;"
                    + "encrypt=true;trustServerCertificate=true;loginTimeout=5";

    @GetMapping("/db-check")
    public String check() {
        try (Connection connection =
                     DriverManager.getConnection(JDBC_URL, "acme_app_prod", "ProdDB#2024!")) {
            return "connected: " + connection.getCatalog();
        } catch (SQLException e) {
            return "error: " + e.getMessage();
        }
    }
}
