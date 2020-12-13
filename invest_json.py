import json
import os
import datetime


# Take the filename and return the absolute path
def makePath(filename):
    return (os.getcwd() + '/' + filename)


# Read the data from the file and return it  as a dictionary
def readJSON(filename):
    path = makePath(filename)
    json_file = open(path, 'r', encoding='utf-8')
    data = json.load(json_file)
    json_file.close()
    return (data)


# Take the dictionary and write it to the file
def writeJSON(data, filename):
    path = makePath(filename)
    json_file = open(path, 'w', encoding='utf-8')
    json.dump(data, json_file, ensure_ascii=False)
    json_file.close()
    print('Data has been written to the ' + filename + ' file')


data = {
    'stocks': {

        'AKSA': {
            'name': 'AKSA Akrilik Kimya Sanayii A.S.',
            'average cost': 5.92,
            'amount': 10.0,
            'price_history': {
                '2020-12-08': {
                    'close': 10.76
                    }
                }
            },

        'ALKA': {
            'name': 'Alkim Kagit Sanayii ve Ticaret A.S.',
            'price': 5.32,
            'amount': 10.0,
            'price_history': {
                '2020-12-08': {
                    'close': 13.2
                    }
                }
            },
        },

    'funds': {

        '835038': {
            'name': 'Kira Sertifikalari Katilim Fonu',
            'average cost': 0.03845,
            'amount': 1000,
            'price_history': {
                '2020-12-08': {
                    'close': 0.038750
                    }
                }
            },

        '835291': {
            'name': 'EUROBOND Borclanma Araclari (Doviz) Fonu',
            'average cost': 8.802,
            'amount': 20,
            'price_history': {
               '2020-12-08': {
                   'close': 9.253359
                   }
                }
            }
        }
    }

writeJSON(data, 'yatirim.json')

# Now we can read and write JSON files
# And we can return the path of a given filename

# After that we need to do;

# Get data from a user, store that data in a organized way, make use of it and save it for later use and present some information acording to user's need

# 1. Get data from a user

def getData(datacategory):
