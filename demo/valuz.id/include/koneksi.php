<?php 

    $servername = "localhost";
    $username = "u5216341_user";
    $password = "@passwordDB#";
    $dbname = "u5216341_valuz";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

function IPnya() {

    $ipaddress = '';

    if (getenv('HTTP_CLIENT_IP'))
        $ipaddress = getenv('HTTP_CLIENT_IP');
    else if(getenv('HTTP_X_FORWARDED_FOR'))
        $ipaddress = getenv('HTTP_X_FORWARDED_FOR');
    else if(getenv('HTTP_X_FORWARDED'))
        $ipaddress = getenv('HTTP_X_FORWARDED');
    else if(getenv('HTTP_FORWARDED_FOR'))
        $ipaddress = getenv('HTTP_FORWARDED_FOR');
    else if(getenv('HTTP_FORWARDED'))
        $ipaddress = getenv('HTTP_FORWARDED');
    else if(getenv('REMOTE_ADDR'))
        $ipaddress = getenv('REMOTE_ADDR');
    else
        $ipaddress = 'IP Tidak Dikenali';
 
    return $ipaddress;

}

function sendwanotif($message, $phone, $type=NULL , $apikey="UPWFgFWC8pD9f3RyRMkjc39hFPRdksTH"){

    $url = 'https://api.wanotif.id/v1/send';
    $curl = curl_init();

    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_HEADER, 0);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 2);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($curl, CURLOPT_TIMEOUT,30);
    curl_setopt($curl, CURLOPT_POST, 1);
    curl_setopt($curl, CURLOPT_POSTFIELDS, array(
        'Apikey'    => $apikey,
        'Phone'     => $phone,
        'Message'   => $message,
    ));
    $response = curl_exec($curl);
    curl_close($curl); 
    
    $data = json_decode($response, true);
    $konek = new mysqli("localhost", "u5216341_user","@passwordDB#", "u5216341_valuz");
    return $konek->query("INSERT INTO `notif` (`wa`, `status`, `type`) VALUES ('$phone', '$response', '$type')");

    //akhir dari pesan wanotif.id

    }

?>