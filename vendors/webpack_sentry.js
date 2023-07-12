var config = {
    plugins: [
        new SentryPlugin({
            // Sentry options are required
            organization: 'your-organization-name',
            project: 'your-project-name',
            apiKey: '1234567890abcdef1234567890abcdef',

            // Release version name/hash is required
            release: process.env.GIT_SHA
        })
    ]
}
