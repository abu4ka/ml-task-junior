# EDA Summary

## Head
|    |   age |   study_hours_per_week |   attendance_rate |   previous_score |   assignments_completed |   sleep_hours |   practice_tests_taken |   late_submissions |   absences |   internet_usage_hours |   social_media_hours | gender   | parent_education   | course_type   | learning_format   | has_part_time_job   | internet_access   |   final_score | risk_level   |   study_efficiency |   discipline_score |   digital_distraction |
|---:|------:|-----------------------:|------------------:|-----------------:|------------------------:|--------------:|-----------------------:|-------------------:|-----------:|-----------------------:|---------------------:|:---------|:-------------------|:--------------|:------------------|:--------------------|:------------------|--------------:|:-------------|-------------------:|-------------------:|----------------------:|
|  0 |    23 |                     61 |                49 |               36 |                      25 |             6 |                      0 |                 27 |         33 |                     14 |                   19 | female   | high_school        | english       | offline           | no                  | yes               |         18.16 | high_risk    |               0.58 |                -98 |                  1.27 |
|  1 |    20 |                     22 |                77 |               42 |                      28 |             3 |                      3 |                  0 |         38 |                     17 |                   14 | male     | high_school        | science       | hybrid            | yes                 | no                |         33.13 | high_risk    |               1.83 |                  1 |                  0.78 |
|  2 |    29 |                      8 |                74 |               39 |                      23 |            12 |                      7 |                 25 |          2 |                     19 |                   15 | female   | high_school        | science       | offline           | no                  | no                |         20.72 | high_risk    |               4.33 |                 -5 |                  0.75 |
|  3 |    27 |                     11 |                 8 |               89 |                      19 |             0 |                      2 |                  6 |          7 |                     12 |                   22 | male     | master             | science       | online            | yes                 | no                |         19.58 | high_risk    |               7.42 |                -24 |                  1.69 |
|  4 |    24 |                      0 |                33 |               54 |                       4 |            11 |                      9 |                 20 |         22 |                      7 |                   12 | male     | bachelor           | programming   | offline           | no                  | yes               |          0    | high_risk    |              54    |                -71 |                  1.5  |

## Describe
|       |       age |   study_hours_per_week |   attendance_rate |   previous_score |   assignments_completed |   sleep_hours |   practice_tests_taken |   late_submissions |   absences |   internet_usage_hours |   social_media_hours |   final_score |   study_efficiency |   discipline_score |   digital_distraction |
|:------|----------:|-----------------------:|------------------:|-----------------:|------------------------:|--------------:|-----------------------:|-------------------:|-----------:|-----------------------:|---------------------:|--------------:|-------------------:|-------------------:|----------------------:|
| count | 500       |               500      |          500      |         500      |               500       |     500       |              500       |          500       |   500      |              500       |            500       |      500      |          500       |           500      |             500       |
| mean  |  22.9     |                38.072  |           48.766  |          50.26   |                13.834   |       6.384   |                9.536   |           14.11    |    24.73   |               11.58    |             12.16    |       42.377  |            3.98094 |           -43.024  |               1.86292 |
| std   |   3.77498 |                23.5419 |           28.9176 |          29.1968 |                 8.60223 |       4.08042 |                5.89017 |            8.74545 |    13.9135 |                7.08661 |              6.82492 |       32.8695 |           10.3226  |            47.1202 |               2.8827  |
| min   |  17       |                 0      |            0      |           0      |                 0       |       0       |                0       |            0       |     0      |                0       |              0       |        0      |            0       |          -171      |               0       |
| 25%   |  20       |                17      |           25      |          25.75   |                 6       |       3       |                4       |            7       |    12      |                5       |              7       |       12.72   |            0.59    |           -74.25   |               0.5     |
| 50%   |  23       |                37      |           48      |          50      |                13.5     |       6       |                9       |           14       |    25      |               12       |             12       |       41.23   |            1.29    |           -40.5    |               0.96    |
| 75%   |  26       |                59.25   |           73      |          76      |                21       |      10       |               15       |           21.25    |    36      |               18       |             18       |       66.1775 |            2.665   |            -9      |               2       |
| max   |  29       |                79      |           99      |          99      |                29       |      13       |               19       |           29       |    49      |               23       |             23       |      100      |           99       |            80      |              23       |

## Risk Level Count
| risk_level   |   count |
|:-------------|--------:|
| high_risk    |     302 |
| low_risk     |     105 |
| medium_risk  |      93 |

## Score by Course Type
| course_type   |   final_score |
|:--------------|--------------:|
| english       |       40.4964 |
| math          |       42.691  |
| programming   |       40.8325 |
| science       |       45.2885 |