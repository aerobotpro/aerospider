<?php
$update_version = '1.0.0.1';
$update_file_name = 'update.exe';
$update_endpoint = 'https://aero-bot.pro/spider/'.$update_file_name;
$announcement = 'Go To SETTINGS > Toggle Probes off as that api is down';
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
ini_set('max_execution_time', 300); //300 seconds = 5 minutes. In case if your CURL is slow and is loading too much (Can be IPv6 problem)
error_reporting(E_ALL);

session_start();
$session_id = session_id();
$servername = "localhost";
$username = "root";
$password = "oggro17$$";
$dbname = "aerobot";
$conn = new mysqli($servername, $username, $password, $dbname);
$my_addr = $_SERVER['HTTP_X_FORWARDED_FOR'];
if (((!isset($_GET['user_key'])) || ((!isset($_GET['client']))))) { 
    header("Location: https://aero-bot.pro");
}else{
    $user_key = $_GET['user_key'];
    $update = $_GET['update'];
    $esc_client =  mysqli_real_escape_string($conn, $_GET['client']);
    $update_redirect = TRUE;
    $query = mysqli_query($conn, "SELECT * FROM spider WHERE user_key='".$user_key."'");
    if(mysqli_num_rows($query) > 0){

        //Existing
        $my_addr_br = '\r\n'.$my_addr;
        $sql = "UPDATE spider SET client='$esc_client', update_version='$update_version', last_login=now(), 
        login_counter = login_counter + 1, last_ip='$my_addr',ip_log=CONCAT(ip_log,'$my_addr_br')
         WHERE user_key='$user_key'";
        if ($conn->query($sql) === TRUE) {
            $sql = "SELECT * FROM spider WHERE user_key='$user_key'";
            $result = mysqli_query($conn, $sql);

            while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)){
                $is_banned = $row['is_banned'];  
                $last_login = $row['last_login'];  
                $login_counter = $row['login_counter'];
            }
            //if ($update !== $update_version){
            //    header("Location: https://aero-bot.pro/update.php");
            //}
            if (intval($is_banned) !== 0){
                echo '{"response":"banned"}';
                die();

            }else{
                echo '{"response":"ok", "update":"'.$update_version.'", "ip":"'.$my_addr.
                    '", "update_file_name":"'.$update_file_name.'", "update_endpoint":"'.$update_endpoint.'", "announcement":"'.$announcement.
                    '", "session_id":"'.$session_id.'", "login_counter":"'.$login_counter.'", "last_login":"'.$last_login.'"}';
            }
        }else{
            echo '{"response":"Fatal Error: '. $sql . "<br>" . $conn->error.'"}';
        }
    }else{

        //Failed Logins
        $sql = "INSERT INTO spider (user_key, client, update_version, last_login,
        login_counter, last_ip, is_paid_user, is_banned)
        VALUES ('ATTEMPTS', '$esc_client', '$update_version', now(), 1 , '$my_addr', 0, 0)";
        if ($conn->query($sql) === TRUE) {
            echo '{"response":"non_existing", "update":"'.$update_version.'", "ip":"'.$my_addr.
                '", "update_file_name":"'.$update_file_name.'", "announcement":"'.$announcement.
                '", "session_id":"'.$session_id.'"}';
        }else{
            echo '{"response":"non_existing"}';
        }
    }   
}
//if ($update_redirect === TRUE){
//    header("Location: ".$update_endpoint);
//    return;
//} 
?>
