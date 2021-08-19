<?php
/*
if(isset($_GET["test"])){
	$output = shell_exec('/root/anaconda3/bin/python3 /home/milesproject2021/abc.py');
	echo $output;
}*/

$command = escapeshellcmd('/usr/bin/python3 /home/milesproject2021/show.py');
$output = shell_exec($command);
echo $output;

?>
