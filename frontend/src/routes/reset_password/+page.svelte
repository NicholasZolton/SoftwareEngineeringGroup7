<script>

</script>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RSVPeats Reset Password</title>
    </head>
    <body>
        <div class="page">
            <div class="heading_bar">
                <span class="company_name">RSVPeats</span>
                <span class="username">Username</span>
            </div>
            <span class="title">Reset Password</span>
            <div class="password">
                <form>
                    <span><input type="text" id="password" name="password" placeholder="Enter new password"></span>
                </form>
            </div>
            <div class="confirm_password">
                <form>
                    <span><input type="text" id="confirm_password" name="confirm_password" placeholder="Confirm new password"></span>
                </form>
            </div>
            <button type="button" id="reset_button" class="button">Reset</button> 
        </div>
    </body>
</html>

<style>
    * {
        box-sizing: border-box;
    }
    body {
        font-size: 14px;
    }
    .page {
        width: 100%;
        height: 720px;
        background: rgba(255,255,255,1);
        opacity: 1;
        position: absolute;
        top: 0px;
        left: 0px;
        overflow: hidden;
    }
    .heading_bar {
        width: 100%;
        height: 52px;
        background: rgba(255,168,0,1);
        opacity: 1;
        position: absolute;
        top: 0px;
        left: 0px;
        overflow: hidden;
    }
    .company_name {
        width: 320px;
        color: rgba(0,0,0,1);
        position: absolute;
        top: 14px;
        left: 18px;
        font-family: Inter;
        font-weight: Regular;
        font-size: 20px;
        opacity: 1;
        text-align: left;
    }
    .username {
        width: 136px;
        color: rgba(0,0,0,1);
        position: absolute;
        top: 16px;
        left: 1144px;
        font-family: Inter;
        font-weight: Regular;
        font-size: 20px;
        opacity: 1;
        text-align: center;
    }
    .title {
        width: 326px;
        color: rgba(255,76,4,1);
        position: absolute;
        top: 230px;
        left: 480px;
        font-family: Inter;
        font-weight: Bold;
        font-size: 42px;
        opacity: 1;
        text-align: center;
    }
    .password {
        width: 560px;
        height: 57px;
        opacity: 1;
        position: absolute;
        top: 330px;
        left: 360px;
        overflow: hidden;
    }
    .confirm_password {
        width: 561px;
        height: 62px;
        opacity: 1;
        position: absolute;
        top: 400px;
        left: 360px;
        overflow: hidden;
    }
    input[type=text] {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #828282;
        border-radius: 4px;
        box-sizing: border-box;
        background: #f2f2f2;
    }
    .button {
        width: 271px;
        height: 39px;
        background: rgba(255,76,4,1);
        opacity: 1;
        position: absolute;
        top: 510px;
        left: 505px;
        border-top-left-radius: 25px;
        border-top-right-radius: 25px;
        border-bottom-left-radius: 25px;
        border-bottom-right-radius: 25px;
        font-size: 18px;
        font-family: Inter;
        overflow: hidden;
    }
</style>


