<?php 
echo '<a href="index.html">BACK TO HOME PAGE</a>';
$login = $_POST['login']; 
$password = $_POST['password'];
if($login == 'admin' && $password ==1234){                   
    $link = @mysql_connect('localhost', 'root','');
if(!$link){ 
    die('Failed to connect to server: ' . mysql_error()); 
}  
    
$db = mysql_select_db('fest'); 
if(!$db) {
	die("Unable to select database"); 
}
$qry="SELECT review,sentiment FROM all_reviews"; 
$result=mysql_query($qry); 
echo '<br>';
echo '<table width=1000 cellpadding=5 cellspacing=4 border=1 bordercolor="Blue" style="border-right-width:1;" align = center> 
    <caption>Fest</caption>
	<th> Review </th> 
    <th> Sentiment </th>';	   
while($row = mysql_fetch_assoc($result)){
	echo '<tr> 
	<td>'.$row['review'].'</td>
    <td>'.$row['sentiment'].'</td>
    </tr>';
}
echo "\n";
echo "\n";
echo "\n";
$db1 = mysql_select_db('intra_college'); 
if(!$db1){
	die("Unable to select database");
}
$qry='SELECT review,sentiment FROM all_reviews'; 
$result=mysql_query($qry); 
echo '<br><br><br><br><br><br><br><br><br><br>';
echo '<table width=1000 cellpadding=5 cellspacing=4 border=1 bordercolor="Blue" style="border-right-width:1;" align = center> 
    <caption>Intra College</caption>
	<th> Review</th> 
    <th> Sentiment </th>';	  
	 
while ($row = mysql_fetch_assoc($result)){
      
    echo '<tr> 

    <td>'.$row['review'].'</td>
    <td>'.$row['sentiment'].'</td>
    </tr>';
	}
"\n";
}

else{
	include("login_form.php");
	echo "<center>Invalid Credentials</center>";
}?>
