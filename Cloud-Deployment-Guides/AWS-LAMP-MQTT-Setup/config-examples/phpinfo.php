<?php
// PHP 資訊測試頁面
// 儲存位置: /var/www/html/info.php
?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP 資訊測試頁面</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>PHP 資訊頁面</h1>
    <p>伺服器時間: <?php echo date("Y-m-d H:i:s"); ?></p>
    <hr>
    <?php phpinfo(); ?>
</body>
</html>
