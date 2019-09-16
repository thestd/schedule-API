# Schedule-API
[![Build Status](http://ci.pnu-bot.pp.ua/buildStatus/icon?job=schedule-API%2Fmaster&style=flat-square)](http://ci.pnu-bot.pp.ua/blue/organizations/jenkins/schedule-API/activity)

A scrapper that works as a server with open api which parse the site of the
[schedule](http://asu.pnu.edu.ua/)

### Main endpoints:
  - `/api/schedule?<parameters>`:
    - method `GET`
    - returns schedule
    - parameters:
      - `group|teacher`:
        - type: `string`
        - required: `True`
        - default: `None`
        - example: `ІПЗ-3`
      - `type`:
        - type: `string`
        - required: `True`
        - default: `None`
        - values: `group`, `teacher`
      - `date_from`:
        - type: `string`
        - required: `False`
        - defaults: `today`
        - example: `dd.mm.yyyy`
      - `date_to`:
        - type: `string`
        - required: `False`
        - defaults: `today`
        - example: `dd.mm.yyyy`
      - response format:
        ```json
          {
            "group": "group name",
            "schedule": [
              {
                "date": "date(dd.mm.yyyy)",
                "day": "day",
                "items": [
                  {
                    "number": "lesson number",
                    "time_bounds": "time_from - time_to",
                    "info": "information"
                  }
                ]
              }
            ]
          }
        ```
      - examples:
        - `yourdomain.com/api/schedule?group=ПІ-4`
        - `yourdomain.com/api/schedule?teacher=Козленко Микола Іванович&date_from=07.05.2019`
        - `yourdomain.com/api/schedule?group=ПІ-4&date_from=08.04.2019&date_to=09.04.2019`
      - response example:
        ```json
         {
          "group": "ПІ-4",
          "schedule": [
            {
              "date": "08.04.2019 ",
              "day": "Понеділок",
              "items": [
                {
                  "number": "1",
                  "time_bounds": "08:30 - 09:50",
                  "info": "Ауд.306 (Центральний корпус, Шевченка 57) Поплавський О.П. Потік ПМ-4, ПІ-4, І-41 Безпека життєдіяльності та цивільний захист (Л) "
                }
              ]
            },
            {
              "date": "09.04.2019 ",
              "day": "Вівторок",
              "items": [
                {
                  "number": "1",
                  "time_bounds": "08:30 - 09:50",
                  "info": "Ауд.320 (Центральний корпус, Шевченка 57) Яновський (п) Ю.М. Збірна група ПІ-4моб. Програмування для iOS (Л) "
                },
                {
                  "number": "2",
                  "time_bounds": "10:05 - 11:25",
                  "info": "Ауд.320б (Центральний корпус, Шевченка 57) Яновський (п) Ю.М. Збірна група ПІ-4моб. Програмування для iOS (Лаб) "
                },
                {
                  "number": "3",
                  "time_bounds": "11:55 - 13:15",
                  "info": "Ауд.320б (Центральний корпус, Шевченка 57) Яновський (п) Ю.М. Збірна група ПІ-4моб. Програмування для iOS (Лаб) "
                },
                {
                  "number": "6",
                  "time_bounds": "16:40 - 18:00",
                  "info": "Ауд.320 (Центральний корпус, Шевченка 57) Козич* О.В. Збірна група ПІ-4веб. Програмування frameworks JavaScript (Л) "
                }
              ]
            }
          ]
        }
        ```
  - `/api/groups?<parameters>`:  
    - method: 'GET'
    - returns: list of groups
    - parameters:
      - `query`:
        - type: `string`
        - required: `True`
        - default: `None`
        - example: `ІПЗ`
    - response format:
      ```json
      [
        "group_name_1",
        "group_name_2",
        ...
        "group_name_n"
      ]
      ```
    - examples:
      - `yourdomain.com/api/groups`
      - `yourdomain.com/api/groups?query=ПІ`
    - response example:
      ```json
      [
        "ПІ-4",
        "ММ-42спів",
        "ММз-42спів",
        "ПОПМОПІ-41",
        "ММз-62спів",
        "ПОІПІнВз24"
      ]
      ```
  - `/api/teachers?<parameters>`:  
    - method: `GET`  
    - returns: list of teachers names
    - parameters:
      - `query`:
        - type: `string`
        - required: `False`
      - `faculty`:
        - type: `int`
        - required: `False`
    - response format:
      ```json
      [
        "name_1",
        "name_2",
        ...
        "name_n"
      ]
      ```
    - examples:
      - `yourdomain.com/api/teachers`
      - `yourdomain.com/api/teachers?query=Коз`
      - `yourdomain.com/api/teachers?faculty=1002`
      - `yourdomain.com/api/teachers?query=Коз&faculty=1002`
    - response example:
      ```json
      [
        "Бушкова (п) Віра Степанівна",
        "Григорук Ірина Іванівна",
        "Жук Ольга Іванівна",
        "Писків (п) Ірина Іванівна",
        "Василишин Ярослава Іванівна"
      ]
      ```
  - `/api/faculties<parameters>`:  
    - method: `GET`  
    - returns: list of faculties with their codes
    - response format:
      ```json
      [
        {
          "name": "Faculty name",
          "code": 1001
        }
      ]
      ```
    - examples:
      - `yourdomain.com/api/faculties`
    - response example:
      ```json
      [
        {
          "name": "Фізико-технічний факультет",
          "code": 1001
        },
        {
          "name": "Факультет математики та інформатики",
          "code": 1002
        },
        {
          "name": "Економічний факультет",
          "code": 1003
        },
        {
          "name": "Інститут післядипломної освіти та довузівської підготовки",
          "code": 1004
        },
        {
          "name": "Коломийський навчально-науковий інститут",
          "code": 1005
        },
        {
          "name": "Навчально-науковий Інститут мистецтв",
          "code": 1006
        },
        {
          "name": "Навчально-науковий Юридичний інститут",
          "code": 1007
        },
        {
          "name": "Педагогічний факультет",
          "code": 1008
        },
        {
          "name": "Факультет іноземних мов",
          "code": 1009
        },
        {
          "name": "Факультет історії, політології і міжнародних відносин",
          "code": 1010
        },
        {
          "name": "Факультет природничих наук",
          "code": 1011
        },
        {
          "name": "Факультет туризму",
          "code": 1012
        },
        {
          "name": "Факультет фізичного виховання і спорту",
          "code": 1013
        },
        {
          "name": "Факультет філології",
          "code": 1014
        },
        {
          "name": "Філософський факультет",
          "code": 1015
        },
        {
          "name": "Загальноуніверситетські кафедри",
          "code": 1016
        },
        {
          "name": "Івано-Франківський коледж",
          "code": 1017
        },
        {
          "name": "Кафедра військової підготовки",
          "code": 1019
        }
      ]
      ```
