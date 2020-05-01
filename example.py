import logging
import logging.config
import yaml


def configure_logger():
    with open('logging.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


def main():
    configure_logger()
    logger = logging.getLogger(__name__)

    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')


if __name__ == "__main__":
    main()
