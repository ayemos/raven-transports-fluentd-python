import os

from raven import Client
from raven_fluentd.transport import FluentdTransport


def main():
    sentry_public_key = os.environ['SENTRY_PUBLIC_KEY']
    sentry_secret_key = os.environ['SENTRY_SECRET_KEY']
    sentry_project_id = os.environ['SENTRY_PROJECT_ID']
    dsn = 'fluentd://%(sentry_public_key)s:%(sentry_secret_key)s@fluentd:24224/%(sentry_project_id)s' \
          % locals()

    client = Client(dsn, transport=FluentdTransport)

    try:
        1 / 0
    except ZeroDivisionError:
        client.captureException()


if __name__ == '__main__':
    main()
