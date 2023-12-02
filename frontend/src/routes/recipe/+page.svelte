<!-- Add Recipe: goes to Event Details -->

<script>

</script>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <div class="page">
            <div class="heading_bar">
                <span class="company_name">RSVPeats</span>
                <span class="username">Username</span>
            </div>
            <span class="title">Recipe</span>
            <div class="ingredients">
                <label for="ingr">Ingredients:</label><br>
                <textarea id="ingr" name="ingr" style="resize: none;" placeholder="List ingredients..." rows="30" cols="50"></textarea>
            </div>
            <div class="instructions">
                <label for="instr">Instructions:</label><br>
                <textarea id="instr" name="instr" style="resize: none;" placeholder="List the steps..." rows="30" cols="90"></textarea>
            </div>
            <button type="button" id="recipe_button" class="button">Save Recipe</button> 

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
        width: 438px;
        color: rgba(255,76,4,1);
        position: absolute;
        top: 70px;
        left: 70px;
        font-family: Inter;
        font-weight: Bold;
        font-size: 42px;
        opacity: 1;
        text-align: left;
    }
    .ingredients {
        width: 380px;
        height: 536px;
        opacity: 1;
        position: absolute;
        top: 144px;
        left: 69px;
        overflow: hidden;
        font-size: 22px;
    }
    .instructions {
        width: 680px;
        height: 536px;
        opacity: 1;
        position: absolute;
        top: 144px;
        left: 516px;
        overflow: hidden;
        font-size: 22px;
    }
    .button {
        width: 249px;
        height: 46px;
        background: rgba(255,193,0,0.6800000071525574);
        opacity: 1;
        position: absolute;
        top: 95px;
        left: 950px;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 20px;
        overflow: hidden;
        font-family: Inter;
        font-weight: Regular;
        font-size: 18px;
        text-align: center;
    }
</style>