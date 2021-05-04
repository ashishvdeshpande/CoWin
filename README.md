# CoWin

- This Application helps user to search Vaccine availibility across india. 
- User can configure search criterial in smaple YAML file (config.yaml). 
- This application searches availibility based on search criterial specified by user.
- If there is vaccine availibility then it starts ringing bell.

Sample yaml format for Search Criteria using PinCode  - Below is sample 

```
pincodesearch:
    -   pincode: 560066
        age: 60
        vaccine: 2
        date: '05-05-2021'
    -   pincode: 560066
        age: 60
        vaccine: 2
        date: '06-05-2021'
    -   pincode: 560066
        age: 60
        vaccine: 2
        date: '07-05-2021'
 ```
 
 In above 
 - pincode : should be valid indian pincode
 - age : integer number age of person In case you want to filter out vaccine for 18+ only.
 - vaccine : enter 1 for COVAXIN 2 for COVISHIELD 3 for Any
 - date : should be in DD-MM-YYYY format (all digit)
  

Above Searches CoviShield vaccine availibility for 45+ on 5th 6th 7th May 2021 on pincode 560066

Sample yaml format for Search Criteria using State and District -  Below is sample

```

stateSearch:
# 18+ vaccine availibility for Bangalore anywhere from 5th 30th May
    -   state_id:   16
        district_id:    294
        age: 38
        vaccine: 3
        date: '05-05-2021'
    -   state_id:   16
        district_id:    294
        age: 38
        vaccine: 3
        date: '06-05-2021'
    -   state_id:   16
        district_id:    294
        age: 38
        vaccine: 3
        date: '07-05-2021'
```

 In above 
 - state_id : valid state id integer. You can get it by running python CoWin_Alert.py -i
 - district_id : valid district id integer for your state. You can get it by running python CoWin_Alert.py -i
 - age : integer number age of person In case you want to filter out vaccine for 18+ only.
 - vaccine : enter 1 for COVAXIN 2 for COVISHIELD 3 for Any
 - date : should be in DD-MM-YYYY format (all digit)

Above Searches Any (COVISHILED/COVAXIN) vaccine availibility for 18+ on 5th 6th 7th May 2021 on in Karnataka state BBMP District.
