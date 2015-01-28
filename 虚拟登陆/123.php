<?php
	require_once ('HttpClient.php');
	$photo = fopen("1.bmp","w");
	$client=HttpClient::quickGet('http://202.117.255.187:8080/reader/login.php');
	$cookie=$client->getCookies();
	$client=new HttpClient('http://202.117.255.187:8080/reader/captcha.php');
	$client->setCookies($cookie,true);
	if (!$client->get('/')) {   
    die('An error occurred: '.$client->getError());   
	}
	echo $client->getContent();
	fwrite($photo,$client->getContent());
	fclose($photo);
?>