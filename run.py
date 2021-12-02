""""Running the ETL application"""
import logging
import logging.config
import yaml


def main():
    """
    entry point to run ETL job
    """
    # Parsing YAML file
    config_path = "./configs/etl_report1_config.yml"
    config = yaml.safe_load(open(config_path))
    # print(config)
    # cconfigure logging
    log_config = config["logging"]
    # dictConfig useful way to log the config as dictionary
    logging.config.dictConfig(log_config)
    # common practice to define logger. __name__ arg shows name of file
    logger = logging.getLogger(__name__)
    logger.info("this is a test")


if __name__ == "__main__":
    main()
