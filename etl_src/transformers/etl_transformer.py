"""ETL Component"""
import logging
from typing import NamedTuple
from etl_src.common.s3 import S3BucketConnector

class ETLSourceConfig(NamedTuple):
    """
    Class for source configuration data

    src_first_extract_date: determines the date for extracting the source
    src_columns: source column names
    src_col_date: column name for date in source
    src_col_isin: column name for isin in source
    src_col_time: name for time in source
    src_col_start_price: col name for starting price in source
    src_col_min_price: col name for min price in source
    src_col_max_price: col name for max price in source
    src_col_traded_vol: col name for traded vol in souurce
    """
    src_first_extract_date: str
    src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price: str
    src_col_min_price: str
    src_col_max_price: str
    src_col_traded_vol: str

class ETLTargetConfig(NamedTuple):
    """
    Class for target configuration data

    trg_col_isin: column name for isin in target
    trg_col_date: column name for date in target
    trg_col_op_price: col name for opening price in target
    trg_col_close_price: col name for closing price in target
    trg_col_min_price: col name for min price in target
    trg_col_max_price: col name for max price in target
    trg_col_daily_traded_vol: col name for daily traded vol in souurce
    trg_col_ch_prev_clos: col name for change to previous day's closing price in target
    trg_key: basic key of target file
    trg_key_date_format: date format of target file key
    trg_format: file format
    """
    trg_col_isin: str
    trg_col_date: str
    trg_col_op_price: str
    trg_col_clos_price: str
    trg_col_min_price: str
    trg_col_max_price: str
    trg_col_daily_traded_vol: str
    trg_col_ch_prev_clos: str
    trg_key: str
    trg_key_date_format: str
    trg_format: str

class TransformETL():
    """
    Reads the source data, transforms and writes the transformed to target
    """
    def __init__(
        self,
        s3_bucket_src: S3BucketConnector,
        s3_bucket_trg: S3BucketConnector,
        meta_key: str,
        src_args: ETLSourceConfig,
        trg_args: ETLTargetConfig
    ):
        """
        Constructor for ETLTransformer

        :param s3_bucket_src: connection to source S3 bucket
        :param s3_bucket_trg: connection to target S3 bucket
        :param meta_key: used as self.meta_key -> key of meta file
        :param src_args: NamedTuple class with source configuration data
        :param trg_args: NamedTuple class with target configuration data
        """
        self._logger = logging.getLogger(__name__)
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date =
        self.extract_date_list = 
        self.meta_update_list = 

    def extract(self):
        pass

    def transform_report1(self):
        pass

    def load(self):
        pass

    def etl_report1(self):
        pass