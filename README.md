# Spreadsheet Analysis

## Data Set Details

The dataset used for this project is from the [University of Washington](http://courses.washington.edu/b517/Datasets/SalaryData.txt) and includes details about the salary of faculty members of the university. The original file was in a .txt format. Here is a sample of what the data looked like:

| case | id | gender | deg | yrdeg | field | startyr | year | rank | admin | salary |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| 1 | 1 | F | Other | 92 | Other | 95 | 95 | Assist | 0 | 6684.000 |
| 2 | 2 | M|Other | 91| Other | 94 | 94 | Assist | 0 | 4743.000 |
| 3 | 2 | M |Other | 91| Other | 94  |  95| Assis | 0 | 4881.000 |
| 4 | 4 | M  | PhD | 96| Other | 95  |  95 |Assist |    0|  4231.000 |
| 5 | 6 | M  | PhD | 66| Other | 91  |  91 |  Full |    1| 11182.000 |
| 6 | 6 | M  | PhD | 66| Other | 91  |  92 |  Full  |   1| 11507.000 |
| 7 | 6 | M |  PhD | 66| Other | 91  |  93 |  Full  |   0| 11840.000 |
| 8 | 6 | M |  PhD | 66| Other | 91 |   94 |  Full  |   0| 11840.000 | 
| 9 | 6 | M |  PhD | 66| Other | 91   | 95 |  Full  |   0| 12184.000 |
| 10 | 7 | M |  PhD | 70| Other | 71  |  76| Assist  |   0 | 1730.000 |
| 11 | 7 | M |  PhD | 70| Other   |    71 |  77 |Assist  |   0|  1851.000 |
| 12 | 7 | M |  PhD | 70| Other  |    71 |  78| Assist   |  0 | 1981.000 |
| 13 | 7 | M  | PhD | 70| Other  |    71 |  79 | Assoc |    0|  2237.000 |
| 14 | 7 | M |  PhD | 70| Other  |    71 |  80 | Assoc |    0 | 2410.000 |
| 15 | 7 | M |  PhD | 70| Other  |    71 |  81 | Assoc|     0 | 2639.000 |
| 16 | 7 | M |  PhD | 70 |Other  |    71 |  82 | Assoc  |   0 | 2639.000 |
| 17 | 7 | M |  PhD | 70| Other  |    71 |  83 | Assoc  |   0 | 2784.000 |
| 18 | 7 | M |  PhD | 70| Other   |   71 |  84|  Assoc  |   0 | 2973.000 |
| 19 | 7 | M |  PhD | 70 |Other   |   71|   85 | Assoc  |   0 | 2973.000 |

## Changes to the Data Set

I had to clean up the data set to make it usable in a csv format, and I also removed unnecessary columns such as the "id" and "admin" columns. Here is some of the code work that shows how I cleaned up the data:

    for v in data:
        data_list.append(v.split())

    for v in range(len(data_list)):
        del data_list[v][1] # removes "case" and "id"
        del data_list[v][8] # removes "admin"

Here are links to the [original text file](https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-aa8690/blob/main/data/salary_data.txt), [cleaned data](https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-aa8690/blob/main/data/clean_data.csv), and [spreadsheet data](https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-aa8690/blob/main/data/clean_data.xlsx). 

## Data Analysis

The cleaned data was opened in Google Sheets, where I did analysis on it. I calculated the average, median, minimum, and maximum for the salaries. The average was $4721.82. The median was $4353.00. The minimum was $1200.00, and the maximum was $14464.00. I then calculated the average and sum for people with arts degrees, which were $3845.62 and $10921563.47 respectively. I then calculated the minimum and maximum for people who had a full arts degree, which was $2018.00 and $9974.00 respectively. My pivot table shows the average salary based on whether an individual had an associates, assist., or full degree. It also shows the average based on if their degree level was not available, along with the total result. Here is the pivot table I created:

|rank|	AVERAGE of salary|
| ---------------------- | ---------------------- |
|Assist|	3388.49682460474|
|Assoc	|3976.50839102466|
|Full	|5835.97778134839|
|NA	|4970|
|Total Result|	4721.82345265764|



