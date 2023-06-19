### Artemis


![Artemis](Artemis.jfif)



## Overview

A tools for Find APK Infrastructure .

Brought to you by:

<img src="https://hadess.io/wp-content/uploads/2022/04/LOGOTYPE-tag-white-.png" alt="HADESS" width="200"/>

[HADESS](https://hadess.io) performs offensive cybersecurity services through infrastructures and software that include vulnerability analysis, scenario attack planning, and implementation of custom integrated preventive projects. We organized our activities around the prevention of corporate, industrial, and laboratory cyber threats.



## Command Line Options
```
          
	  --help                       Display help
	  --path  					   Required path of apk file
	  --manifest  				   Display manifest informations
	  --infra  					   Find all infra addresses included ip,domain ex. --infra ip,domain
	  --whoise  				   Whoise all infra included ip,domain ex. --whoise ip,domain
	  --output  				   Set output files ex. --output out.txt
	 
```

Example Usage:

1.Find infra(domain and ip) in sample4.apk and set output result into out.txt

```
python3 main.py --path sample4.apk --infra domain,ip --output out.txt
```
