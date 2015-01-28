<?php
$cookie_file = "tmp.cookie";
$xh = 2012302612;
$login_url = "http://222.24.192.69/loginAction.do?dlfs=mh&mh_zjh=2013300382&mh_mm=WTAWLC";
$verify_code_url = "http://222.24.192.69/gradeLnAllAction.do?type=ln&oper=qbinfo&cjbh=".$xh;
$curl = curl_init();
$timeout = 5;
curl_setopt($curl, CURLOPT_URL, $login_url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_CONNECTTIMEOUT, $timeout);
curl_setopt($curl,CURLOPT_COOKIEJAR,$cookie_file); //获取COOKIE并存储
$contents = curl_exec($curl);
curl_close($curl);

$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $verify_code_url);
curl_setopt($curl, CURLOPT_COOKIEFILE, $cookie_file);
curl_setopt($curl, CURLOPT_HEADER, 0);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
$img = curl_exec($curl);
curl_close($curl);

echo $verify_code_url;

