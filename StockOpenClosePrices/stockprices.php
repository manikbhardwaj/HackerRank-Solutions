<?php
/*
 * Complete the 'test' function below.
 *
 * The function accepts following parameters:
 *  1. STRING firstDate
 *  2. STRING secondDate
 *  3. STRING dayOfWeek
 */

function test($firstDate, $secondDate, $dayOfWeek)
{
    file_get_contents('https://jsonmock.hackerrank.com/api/stocks');
    $weekdays = array("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday");
    $startDate = strtotime('5-January-2000');
    $endDate = strtotime('1-January-2014');
    $from = strtotime($firstDate);
    $to = strtotime($secondDate);
    if ($from < $startDate) {
        $from = $startDate;
    }
    if ($to > $endDate) {
        $to = $endDate;
    }
    if (!in_array($dayOfWeek, $weekdays)) {
        echo "out of paramaters";
    } else {
        do {
            $tempDate = strtotime("{$dayOfWeek}", $from);
            $url = "https://jsonmock.hackerrank.com/api/stocks/?date=".date('j-F-Y', $tempDate);
            $theResponse = file_get_contents($url);
            $result = json_decode($theResponse);
            if ($result->total==0) {
                $from = strtotime("+7 day", $tempDate);
            } else {
                foreach ($result->data as $res) {
                    echo $res->date." ".$res->open." ".$res->close."\n";
                    $from = strtotime("+7 day", $tempDate);
                }
            }
        } while ($from < $to);
    }
}


//2-June-2000 21-June-2000 Monday

$firstDate = "1-January-2000";

$secondDate = "22-February-2000";

$dayOfWeek = "Monday";

test($firstDate, $secondDate, $dayOfWeek);
