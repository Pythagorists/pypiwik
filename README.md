pypiwik
=======

A simple Python wrapper for the Piwik API.

# Rationale

Existing Piwik API wrappers for Python - and for that matter, all languages -
focused on providing access into Piwik's Tracking API. Some also provide access
for the Reporting API, but none were available that addressed the need to
programmatically manage Piwik installations.

While embedding Piwik into a third-party application to enable analtyics for
user-created content, I wrote quite a bit of code based on
[requests](http://github.com/kennethreitz/requests) to manage both users and
sites dynamically. This code was difficult to tests, so it was refactored into
pypiwik. At the same time, the effort was made to use current best practices
regarding coding style, full test coverage, continuous integration, and support
for multiple versions of Python.

This package is not yet complete, and will likely not be for some time. It has
been released in the hopes that it will make life easier for developers facing
similar tasks, and that it will be improved and expanded by the community if
there is in fact a need for it.

# Quickstart

Connect to a running Piwik server:

    import pypiwik
    
    connection = pypiwik.Server(
        url='piwik.mydomain.com',
        auth_token='6a110eba31b4424558fb00c2a76f7380',
    )
   
    print(connection.version)
    > 2.7.0