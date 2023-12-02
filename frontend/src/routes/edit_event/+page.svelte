<!-- Edit Event: goes to Event Admin -->

<script>
    import map from "$lib/assets/map.png";
</script>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RSVPeats Edit Your Event</title>
    </head>
    <body>
        <div class="page">
            <div class="heading_bar">
                <span class="company_name">RSVPeats</span>
                <span class="username">Username</span>
            </div>
            <span class="title">Edit Your Event</span>
            <div class="event_name">
                <form>
                    <span><input type="text" id="name" name="name" placeholder="Enter event name"></span>
                </form>
            </div>
            <div class="calendar">
                <div class="v79_17">
                    <div class="v79_18">
                        <!-- <div class="v79_19">
                            <div class="v79_20"></div>
                        </div> -->
                        <span class="v79_21">February 2021</span>
                        <div class="v79_22">
                            <div class="v79_23"></div>
                        </div>
                    </div>
                    <div class="v79_24">
                        <div class="v79_25">
                            <span class="v79_26">MON</span>
                            <span class="v79_27">1</span>
                            <span class="v79_28">8</span>
                            <span class="v79_29">15</span>
                            <span class="v79_30">22</span>
                            <span class="v79_31">29</span>
                        </div>
                        <div class="v79_32">
                            <span class="v79_33">TUE</span>
                            <span class="v79_34">2</span>
                            <span class="v79_35">9</span>
                            <span class="v79_36">16</span>
                            <span class="v79_37">23</span>
                            <span class="v79_38">30</span>
                        </div>
                        <div class="v79_39">
                            <span class="v79_40">WED</span>
                            <span class="v79_41">3</span>
                            <span class="v79_42">10</span>
                            <span class="v79_43">17</span>
                            <span class="v79_44">24</span>
                            <span class="v79_45">31</span>
                        </div>
                        <div class="v79_46">
                            <span class="v79_47">THU</span>
                            <span class="v79_48">4</span><span class="v79_49">11</span>
                            <span class="v79_50">18</span>
                            <span class="v79_51">25</span>
                            <span class="v79_52">1</span>
                        </div>
                        <div class="v79_53">
                            <span class="v79_54">FRI</span>
                            <span class="v79_55">5</span>
                            <span class="v79_56">12</span>
                            <span class="v79_57">19</span>
                            <span class="v79_58">26</span>
                            <span class="v79_59">2</span>
                        </div>
                        <div class="v79_60">
                            <span class="v79_61">SAT</span>
                            <span class="v79_62">6</span>
                            <span class="v79_63">13</span>
                            <span class="v79_64">20</span>
                            <span class="v79_65">27</span>
                            <span class="v79_66">3</span>
                        </div><div class="v79_67">
                            <span class="v79_68">SUN</span>
                            <span class="v79_69">7</span>
                            <span class="v79_70">14</span>
                            <span class="v79_71">21</span>
                            <span class="v79_72">28</span>
                            <span class="v79_73">4</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="mult_days">
                <!-- <label class="container">Multiple Day Event
                    <input type="checkbox">
                    <span class="checkmark"></span>
                </label> -->
                <span><input type="checkbox" id="mult_days" name="mult_days"></span>
                <label for="mult_days"> Multiple Day Event</label><br>
                <input type="text" id="start_date" name="start_date" placeholder="start date">
                <span>to</span>
                <input type="text" id="end_date" name="end_date" placeholder="end date">
            </div>
            <div class="times">
                <label for="start_time">Start Time:</label>
                <input type="text" id="start_time" name="start_time"><br><br>
                <label for="end_time">End Time:</label>
                <input type="text" id="end_time" name="end_time">
            </div>
            <div class="select_buttons">
                <input type="radio" id="public" name="event_type">
                <label for="public"> Public Event</label><br>
                <input type="radio" id="private" name="event_type">
                <label for="private"> Invite Only</label><br><br>
            </div>
            <img src={map} alt="event location on map"/>
            <div class="description">
                <textarea id="descr" name="descr" style="resize: none;" placeholder="Enter event description..." rows="5" cols="50"></textarea>
            </div>
            <button type="button" id="edit_button" class="button">Save Changes</button> 
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
    .event_name {
        width: 534px;
        height: 33px;
        background: rgb(255, 255, 255);
        opacity: 1;
        position: absolute;
        top: 141px;
        left: 114px;
        overflow: hidden;
    }
    .mult_days {
        width: 500px;
        height: 50px;
        background: rgba(255,255,255,1);
        font-size: 17px;
        opacity: 1;
        margin: 5px;
        position: absolute;
        top: 460px;
        left: 115px;
        overflow: hidden;
    }
    .times {
        width: 260px;
        color: rgba(0,0,0,1);
        position: absolute;
        top: 563px;
        left: 120px;
        font-family: Inter;
        font-weight: Regular;
        font-size: 18px;
        opacity: 1;
        text-align: right;
    }
    .select_buttons {
        width: 200px;
        height: 100px;
        background: rgba(255,255,255,1);
        font-size: 18px;
        opacity: 1;
        position: absolute;
        top: 550px;
        left: 470px;
        margin: 5px;
        overflow: hidden;
    }
    img {
        width: 390px;
        height: 286px;
        background-repeat: no-repeat;
        background-position: center center;
        background-size: cover;
        opacity: 1;
        position: absolute;
        top: 131px;
        left: 777px;
        border: 1px solid rgba(0,0,0,1);
        overflow: hidden;
    }
    .description {
        width: 390px;
        height: 147px;
        opacity: 1;
        position: absolute;
        top: 441px;
        left: 777px;
        overflow: hidden;
        text-align: center;
    }
    .button {
        width: 249px;
        height: 46px;
        background: rgba(255,193,0,0.6800000071525574);
        opacity: 1;
        position: absolute;
        top: 600px;
        left: 854px;
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



    .v79_17 {
    width: 534px;
    height: 265px;
    background: rgba(255,255,255,1);
    padding: 16px 16px;
    /* margin: 20px; */
    opacity: 1;
    position: absolute;
    top: 182px;
    left: 114px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    overflow: hidden;
    }
    .v79_18 {
    width: 502px;
    height: 24px;
    background: url("../images/v79_18.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 16px;
    left: 16px;
    overflow: hidden;
    }
    /* .v79_19 {
    width: 24px;
    height: 24px;
    background: rgba(234,234,239,1);
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 0px;
    border-top-left-radius: 100px;
    border-top-right-radius: 100px;
    border-bottom-left-radius: 100px;
    border-bottom-right-radius: 100px;
    overflow: hidden;
    }
    .v79_20 {
    width: 7px;
    height: 9px;
    background: url("../images/v79_20.png");
    opacity: 1;
    position: absolute;
    top: 7px;
    left: 9px;
    border: 1px solid rgba(0,0,0,1);
    } */
    .v79_21 {
    width: 120px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 3px;
    left: 202px;
    font-family: Inter;
    font-weight: Bold;
    font-size: 14px;
    opacity: 1;
    text-align: left;
    }
    .v79_22 {
    width: 24px;
    height: 24px;
    background: rgba(234,234,239,1);
    opacity: 1;
    position: absolute;
    top: 24px;
    left: 502px;
    border-top-left-radius: 100px;
    border-top-right-radius: 100px;
    border-bottom-left-radius: 100px;
    border-bottom-right-radius: 100px;
    transform: rotate(-180deg);
    overflow: hidden;
    }
    .v79_23 {
    width: 7px;
    height: 9px;
    background: url("../images/v79_23.png");
    opacity: 1;
    position: absolute;
    top: 8px;
    left: 8px;
    border: 1px solid rgba(0,0,0,1);
    }
    .v79_24 {
    width: 502px;
    height: 189px;
    background: url("../images/v79_24.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 60px;
    left: 16px;
    overflow: hidden;
    }
    .v79_25 {
    width: 29px;
    height: 189px;
    background: url("../images/v79_25.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 0px;
    overflow: hidden;
    }
    .v79_26 {
    width: 29px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 0px;
    left: 0px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 12px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_27 {
    width: 7px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 26px;
    left: 11px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_28 {
    width: 10px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 61px;
    left: 10px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_29 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 96px;
    left: 6px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_30 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 131px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_31 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 166px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_32 {
    width: 24px;
    height: 189px;
    background: url("../images/v79_32.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 84px;
    overflow: hidden;
    }
    .v79_33 {
    width: 24px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 0px;
    left: 0px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 12px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_34 {
    width: 10px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 26px;
    left: 7px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_35 {
    width: 10px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 61px;
    left: 7px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_36 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 96px;
    left: 4px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_37 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 131px;
    left: 3px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_38 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 166px;
    left: 3px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_39 {
    width: 28px;
    height: 189px;
    background: url("../images/v79_39.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 162px;
    overflow: hidden;
    }
    .v79_40 {
    width: 28px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 0px;
    left: 0px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 12px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_41 {
    width: 10px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 26px;
    left: 9px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_42 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 61px;
    left: 6px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_43 {
    width: 16px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 96px;
    left: 6px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_44 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 131px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_45 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 166px;
    left: 6px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_46 {
    width: 26px;
    height: 189px;
    background: url("../images/v79_46.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 245px;
    overflow: hidden;
    }
    .v79_47 {
    width: 26px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 0px;
    left: 0px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 12px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_48 {
    width: 10px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 27px;
    left: 8px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_49 {
    width: 14px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 62px;
    left: 6px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_50 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 97px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_51 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 132px;
    left: 4px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_52 {
    width: 7px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 168px;
    left: 10px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 14px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_53 {
    width: 19px;
    height: 189px;
    background: url("../images/v79_53.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 325px;
    overflow: hidden;
    }
    .v79_54 {
    width: 18px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 0px;
    left: 1px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 12px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_55 {
    width: 10px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 27px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_56 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 62px;
    left: 1px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_57 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 97px;
    left: 1px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_58 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 132px;
    left: 0px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_59 {
    width: 9px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 168px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 14px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_60 {
    width: 23px;
    height: 189px;
    background: url("../images/v79_60.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 399px;
    overflow: hidden;
    }
    .v79_61 {
    width: 23px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 0px;
    left: 0px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 12px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_62 {
    width: 10px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 27px;
    left: 7px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_63 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 62px;
    left: 3px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_64 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 97px;
    left: 2px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_65 {
    width: 18px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 132px;
    left: 3px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_66 {
    width: 9px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 168px;
    left: 7px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 14px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_67 {
    width: 26px;
    height: 189px;
    background: url("../images/v79_67.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    opacity: 1;
    position: absolute;
    top: 0px;
    left: 476px;
    overflow: hidden;
    }
    .v79_68 {
    width: 26px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 0px;
    left: 0px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 12px;
    opacity: 0.5;
    text-align: left;
    }
    .v79_69 {
    width: 9px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 27px;
    left: 9px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_70 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 62px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_71 {
    width: 17px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 97px;
    left: 5px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_72 {
    width: 19px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 132px;
    left: 4px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 15px;
    opacity: 1;
    text-align: left;
    }
    .v79_73 {
    width: 9px;
    color: rgba(0,0,0,1);
    position: absolute;
    top: 168px;
    left: 9px;
    font-family: Inter;
    font-weight: Regular;
    font-size: 14px;
    opacity: 0.5;
    text-align: left;
    }
</style>


