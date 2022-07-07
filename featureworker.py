# -*- coding: utf-8 -*-
# Create new features
import pandas as pd
import numpy as np
import time

class FeatureWorkerClass(object):
    def __init__(self, target_code):
        self.target_col = target_code

    # create lag features
    @staticmethod
    def create_lag_features(df, target_col, lags):
        lag_df = df.copy()
        for i in lags:
            lag_df[f'{target_col}_lag_{i}'] = lag_df[target_col].shift(i).values
        return lag_df

    # create rolling features: mean, max, min, median, std
    @staticmethod
    def create_rolling_features(df, target_col, windows, min_periods=1, shift=1):
        rolling_shift_df = df.copy()
        for w in windows:
            shift_df = rolling_shift_df[target_col].shift(shift).rolling(
                window=w, 
                min_periods=min_periods
                ).agg([ 'max', 'mean', 'min', 'median', np.nanstd], axis=1
                ).rename(columns={
                        'max': "_rmax_{}".format(w),
                        'mean': "_rmean_{}".format(w),
                        'min': "_rmin_{}".format(w),
                        'median': "_rmedian_{}".format(w),
                        'nanstd': "_rstd_{}".format(w),
                        }).reset_index()
            shift_df.columns = [''.join(col) for col in shift_df.columns]
            del shift_df['index']
            rolling_shift_df[list(shift_df.columns)] = shift_df
            
        return rolling_shift_df

    # create rolling skew features
    @staticmethod
    def create_rskew_features(df, target_col, windows, min_periods=2, shift=1):
        rolling_rskew_df = df.copy()
        for w in windows:
            rolling_rskew_df[f'{target_col}_rskew_{w}'] = \
                rolling_rskew_df[target_col].shift(shift).rolling(
                    window=w,
                    min_periods=min_periods
                ).skew().fillna(0).values
        return rolling_rskew_df

    # create diff features
    @staticmethod
    def create_diff_features(df, target_col, periods=[1], shift=1):
        diff_df = df.copy()
        for p in periods:
            diff_df[f'{target_col}_diff_{p}'] = \
                diff_df[target_col].shift(shift).diff(periods=p).abs().values
        return diff_df

    # create percentage change features
    @staticmethod
    def create_pct_change_features(df, target_col, periods=[1], shift=1):
        pct_change_df = df.copy()
        for p in periods:
            pct_change_df[f'{target_col}_pct_change_{p}'] = \
                pct_change_df[target_col].shift(shift).pct_change(periods=p).replace(np.inf,0).fillna(0).abs().values
        return pct_change_df

    # Creating exponentially weighted mean features
    @staticmethod
    def create_ewm_features(df, target_col, alpha=[0.9], shift=[1]):
        ewm_df = df.copy()
        for a in alpha:
            for s in shift:
                ewm_df[f'{target_col}_ewm_{a}_{s}'] = \
                    ewm_df[target_col].shift(s).ewm(alpha=a).mean().values
        return ewm_df
    
    @staticmethod
    def create_kdj_features(df, target_col, min_periods=2, windows=[10], com=[2]):
        kdj_df = df.copy()
        for c in com:
            for w in windows:
                lowest = kdj_df[target_col].shift(1).rolling(window=w, min_periods=min_periods).min()
                highest = kdj_df[target_col].shift(1).rolling(window=w, min_periods=min_periods).max()
                rsv = (kdj_df[target_col].shift(1) - lowest) / (highest - lowest) * 100
                rsv.fillna(value = 100.0, inplace=True)

                k = rsv.ewm(com=c, adjust=False).mean()
                kdj_df[f'{target_col}_kdj_{c}_{w}'] = 3 * k - 2 * k.ewm(com=c, adjust=False).mean()
        return kdj_df

    def create_waybill_features(self, df):
        matrix_df = df.copy()
        matrix_df = self.create_lag_features(df=matrix_df,
                                             target_col=self.target_col,
                                             lags=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 20, 23, 24, 25, 47, 48, 49, 50,51,52,53,54,55,56])
        print("lag feature over.......................") 
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

 
        matrix_df = self.create_rolling_features(df=matrix_df,
                                                    target_col=self.target_col,
                                                    shift=1,
                                                    windows=[2, 3, 4, 8, 12, 16, 48])
        print("rolling feature over.......................")
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

        matrix_df = self.create_pct_change_features(df=matrix_df,
                                                    target_col=self.target_col,
                                                    shift=1,
                                                    periods=[1, 4, 8, 12, 16])
        print("pct change feature over.......................")
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


        matrix_df = self.create_ewm_features(df=matrix_df,
                                             target_col=self.target_col,
                                             alpha=[0.95, 0.5],
                                             shift=[1, 4, 8, 12, 16])
        print("ewm feature over.......................")
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        
        matrix_df = self.create_rskew_features(df=matrix_df,
                                             target_col=self.target_col,
                                             windows=[2, 3, 4, 8, 12, 16, 48], 
                                             min_periods=2, 
                                             shift=1)
        print("rskew feature over.......................")
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        
        matrix_df = self.create_kdj_features(df=matrix_df,
                                             target_col=self.target_col,
                                             min_periods=2, 
                                             windows=[7, 10, 20, 30], 
                                             com=[1, 2])
        print("kdj feature over.......................")
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        
        return matrix_df
