import os
import csv


with open('C:\\Users\\BVitkaus\\Documents\\TutorDeactivate2.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        #print(row)  #Row is an array
        names = row[0] + ' ' + row[1]
        print(names)
        os.system('drush --yes -r $your-path-to-drupal -l $your-site-url user-cancel --delete-content %s > /dev/null' % names)