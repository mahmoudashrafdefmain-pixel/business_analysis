@echo off
title Recreating All E-Commerce Analytics Datasets on D: Disk
echo ====================================================================
echo  Launching Master Data Gathering & Combining Pipeline
echo  Target: D:\ecommerce_analytics_datasets\
echo ====================================================================
echo.
"D:\Python\Python312\python.exe" "D:\ecommerce_analytics_datasets\Gathring_Code\run_all_gatherings.py"
echo.
echo ====================================================================
echo  Pipeline Execution Finished!
echo ====================================================================
pause
