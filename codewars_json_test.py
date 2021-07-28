x = {
 "class": "dataset",
 "dimension": {
  "geo": {
   "category": {
    "index": {
     "AT": 0,
     "BE": 1,
     "BG": 2,
     "CH": 3,
     "CY": 4,
     "CZ": 5,
     "DE": 6,
     "DK": 7,
     "EA": 8,
     "EA19": 9,
     "EE": 10,
     "EL": 11,
     "ES": 12,
     "EU27_2020": 13,
     "EU28": 14,
     "FI": 15,
     "FR": 16,
     "HR": 17,
     "HU": 18,
     "IE": 19,
     "IT": 20,
     "LT": 21,
     "LU": 22,
     "LV": 23,
     "MT": 24,
     "NL": 25,
     "NO": 26,
     "PL": 27,
     "PT": 28,
     "RO": 29,
     "RS": 30,
     "SE": 31,
     "SI": 32,
     "SK": 33,
     "TR": 34,
     "UK": 35
    },
    "label": {
     "AT": "Austria",
     "BE": "Belgium",
     "BG": "Bulgaria",
     "CH": "Switzerland",
     "CY": "Cyprus",
     "CZ": "Czechia",
     "DE": "Germany (until 1990 former territory of the FRG)",
     "DK": "Denmark",
     "EA": "Euro area (EA11-1999, EA12-2001, EA13-2007, EA15-2008, EA16-2009, EA17-2011, EA18-2014, EA19-2015)",
     "EA19": "Euro area - 19 countries  (from 2015)",
     "EE": "Estonia",
     "EL": "Greece",
     "ES": "Spain",
     "EU27_2020": "European Union - 27 countries (from 2020)",
     "EU28": "European Union - 28 countries (2013-2020)",
     "FI": "Finland",
     "FR": "France",
     "HR": "Croatia",
     "HU": "Hungary",
     "IE": "Ireland",
     "IT": "Italy",
     "LT": "Lithuania",
     "LU": "Luxembourg",
     "LV": "Latvia",
     "MT": "Malta",
     "NL": "Netherlands",
     "NO": "Norway",
     "PL": "Poland",
     "PT": "Portugal",
     "RO": "Romania",
     "RS": "Serbia",
     "SE": "Sweden",
     "SI": "Slovenia",
     "SK": "Slovakia",
     "TR": "Turkey",
     "UK": "United Kingdom"
    }
   },
   "label": "geo"
  },
  "na_item": {
   "category": {
    "index": {
     "B1GQ": 0
    },
    "label": {
     "B1GQ": "Gross domestic product at market prices"
    }
   },
   "label": "na_item"
  },
  "s_adj": {
   "category": {
    "index": {
     "SCA": 0
    },
    "label": {
     "SCA": "Seasonally and calendar adjusted data"
    }
   },
   "label": "s_adj"
  },
  "time": {
   "category": {
    "index": {
     "2018Q2": 0,
     "2018Q3": 1,
     "2018Q4": 2,
     "2019Q1": 3,
     "2019Q2": 4,
     "2019Q3": 5,
     "2019Q4": 6,
     "2020Q1": 7,
     "2020Q2": 8,
     "2020Q3": 9,
     "2020Q4": 10,
     "2021Q1": 11
    },
    "label": {
     "2018Q2": "2018Q2",
     "2018Q3": "2018Q3",
     "2018Q4": "2018Q4",
     "2019Q1": "2019Q1",
     "2019Q2": "2019Q2",
     "2019Q3": "2019Q3",
     "2019Q4": "2019Q4",
     "2020Q1": "2020Q1",
     "2020Q2": "2020Q2",
     "2020Q3": "2020Q3",
     "2020Q4": "2020Q4",
     "2021Q1": "2021Q1"
    }
   },
   "label": "time"
  },
  "unit": {
   "category": {
    "index": {
     "MIO_EUR_SCA": 0
    },
    "label": {
     "MIO_EUR_SCA": "Million euro (SCA)"
    }
   },
   "label": "unit"
  }
 }
 }

print(list(y for y in x.items()))
