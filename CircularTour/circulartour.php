<?php

function optimalPoint($magic, $dist)
{
    $last = 1;
    $position = 0;
    $minimumMagic = 1;
    $minimumPosition = 0;
    $n = count($magic);

    $curr_magic = $magic[$position] - $dist[$position];

    while ($last != $position || $curr_magic < 0) {
        while ($curr_magic < 0 && $position != $last) {
            $curr_magic -= $magic[$position] - $dist[$position];
            $position = ($position + 1) % $n;
            // If 0 is being considered as start again, then there is no
            // possible solution
            if ($position == 0) {
                return -1;
            }
        }
        $curr_magic += $magic[$last] - $dist[$last];

        $last = ($last + 1) % $n;
    }
    return $position;
}

$magic =  array(8,4,1,9);
$dist = array(10,9,3,5);

$data = optimalPoint($magic, $dist);
echo $data;
