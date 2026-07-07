from flask import Flask, request, Response
from flask import g, abort
import zlib
import msgpack
from Crypto.Cipher import Blowfish
from binascii import unhexlify
from decorators import encrypt_response
import json
import os  # <-- EKSİK OLAN VE ÇÖKMEYE SEBEP OLAN IMPORT BUYDU!
from myclub import build_entry_response

KEY_HEX = "a2df2319c1e5ec1e206a724b5709de77b728609eedbbfaaa939ab3d7bb4d7f77c135147cb76b4c2efa0249fad843a9d5cc38cae19cc41c90"
KEY = unhexlify(KEY_HEX)

IV_LENGTH = 8

app = Flask(__name__)

# Tüm dosya yollarını server.py'nin konumuna göre dinamik yapan yardımcı fonksiyon
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_json_response(filename):
    json_path = os.path.join(BASE_DIR, "responses", filename)
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


@app.before_request
def decrypt_and_unpack():
    body = request.get_data()
    if len(body) < IV_LENGTH:
        abort(400)
    iv = body[:IV_LENGTH]
    ciphertext = body[IV_LENGTH:]

    cipher = Blowfish.new(KEY, Blowfish.MODE_CBC, iv=iv)
    try:
        plain = cipher.decrypt(ciphertext)
    except Exception:
        abort(400)

    try:
        decompressed = zlib.decompress(plain)
    except zlib.error:
        abort(400)

    try:
        g.unpacked = msgpack.unpackb(decompressed)
    except Exception:
        abort(400)

@app.route("/auc/02_03_03/CmdGetServerEnv.php", methods=["POST"])
@encrypt_response
def cmd_get_server_env():
    result_str = str(g.unpacked)
    print("[DECRYPTED]", result_str, flush=True)
    app.logger.info(f"Decrypted result: {result_str}")

    response = {
        "msgid": "CMD_GET_SERVER_ENV",
        "result": "NOERR",
        "proto_opt": "eyJEZXZpY2UiOlt7IkVuYWJsZU1hbnVmYWN0dXJlTW9kZWxOYW1lUHJlc2V0VHlwZSI6MCwiTGlzdGVuZXJXb3JrZXJDb25maWdQcmVzZXRUeXBlIjowfSx7IkVuYWJsZU1hbnVmYWN0dXJlTW9kZWxOYW1lUHJlc2V0VHlwZSI6MSwiTGlzdGVuZXJXb3JrZXJDb25maWdQcmVzZXRUeXBlIjoxfSx7IkVuYWJsZU1hbnVmYWN0dXJlTW9kZWxOYW1lUHJlc2V0VHlwZSI6MiwiQXBwWWllbGRDb25maWdQcmVzZXRUeXBlIjowfV0sIkNTIjp7Ik5ldHdvcmsiOnsiQ21wTmV0d29ya0lvVmVyc2lvbiI6MCwiRGNUZXN0UHJvYmVEYXRhTGVuZ3RoIjoyLCJEY1Rlc3RVZHBQaW5nUmVxdWVzdExlbmd0aCI6MiwiRGNUZXN0Rm9yQ2xpZW50U2VydmVyTW9kZVJlY29tbWVuZGVkUmVnaW9uTW9kZSI6MiwiRGNUZXN0Rm9yQ2xpZW50U2VydmVyTW9kZVJlY29tbWVuZGVkUmVnaW9uVGhyZXNob2xkIjoxMH0sIk1hdGNoQ29tbWFuZEJ1ZmZlcmluZ0NvbnRyb2wiOnsiUHJlZGljdEtlZXBCdWZmZXJTaXplRGVsdGFGcm9tTWF0Y2hTdG9wQ291bnRFbmFibGUiOmZhbHNlfSwiTWF0Y2giOnsiTm9Nb3ZlT3BlcmF0aW9uVGltZW91dE1zIjoxMjAwMDB9fSwiUDJQIjp7Ik1hdGNoIjp7Ik5vTW92ZU9wZXJhdGlvblRpbWVvdXRNcyI6MTIwMDAwfX19",
        "is_revision_check": "NO",
        "enable_gpu_skinning": "false",
        "eula_version_jp": "1.0.0",
        "eula_version_eea": "1.0.0",
        "eula_version_other": "1.0.0",
        "privacy_notice_version_info": "1",
        "data_version": "1.0.0",
        "challenge_code": "950a62c510bdf7900b7dd70a8475e396",
        "ip_country_code": "TUN",
        "notification_url": "https://konami.net/",
        "page_timestamp": 1783004905,
        "url_num": 0,
        "player_level_max": 100,
        "energy_recovery_rate": 60,
        "lottery_effect_setting": {
            "m_effect_rate": 100,
            "m_lightning_threshold": 50,
            "m_lightning_rate": 10,
        },
        "match_tutorial_setting": [1, 2, 3],
        "license_out_player_list": [
            {"serial": 12345678901234, "id": 1},
        ],
        "license_out_coach_list": [1, 2],
        "ulist": [
            {"type": "EULA_PES", "url": "https://legal.konami.com/games/efootball/terms/tou/202603/en-us.html"},
            {"type": "EULA_MYCLUB", "url": "https://legal.konami.com/games/efootball/terms/vc/en-us.html"},
            {"type": "EULA_PRIVACY_POLICY", "url": "https://legal.konami.com/games/privacy/view/en/"},
            {"type": "EULA_PRIVACY_NOTICE", "url": "https://legal.konami.com/games/games4gdpr/view/en-us/"},
            {"type": "EULA_PRIVACY_POLICY_CALIFORNIA", "url": "https://legal.konami.com/games/games4ccpa/view/en-us/"},
            {"type": "EULA_PRIVACY_POLICY_JAPAN", "url": "https://legal.konami.com/games/privacy-jp/view/en-us/"},
            {"type": "EULA_PES_JAPAN", "url": "https://legal.konami.com/games/efootball/terms/tou/202603/en-us-jp.html"},
            {"type": "EULA_MYCLUB_JAPAN", "url": "https://legal.konami.com/games/efootball/terms/vc/en-us-jp.html"},
            {"type": "ANDROID_ADVERTISING_ID", "url": "https://legal.konami.com/games/android/terms/ad_attention/en/"},
            {"type": "EULA_PRIVACY_COLLECT_AND_USE_KOREA", "url": "https://legal.konami.com/games/efootball/n4ko/consent1/view/en-us/"},
            {"type": "EULA_PRIVACY_POLICY_THAILAND", "url": "https://legal.konami.com/games/privacy/th/"},
            {"type": "EULA_FUND_LAW_JAPAN", "url": "https://legal.konami.com/games/efootball/terms/psa/en-us/index_202602.html"},
            {"type": "EULA_COMMERCIAL_LAW_JAPAN", "url": "https://legal.konami.com/kde/notice/sct/en/"},
            {"type": "EULA_PRIVACY_NOTICE_KOREA", "url": "https://legal.konami.com/games/efootball/n4ko/view/en-us/"},
            {"type": "IMAGE_DATA", "url": "https://d1ln4m3c7n87ju.cloudfront.net/prd"},
            {"type": "ONLINE_AD", "url": "https://d1ln4m3c7n87ju.cloudfront.net/prd"},
            {"type": "INQUIRY_BASE", "url": "https://www.konami.com/efootball/mobile_support/"},
            {"type": "OPT_OUT", "url": "https://legal.konami.com/games/information/optout/"},
            {"type": "E_FOOTBALL_POINT_SITE", "url": "https://efootball-point.konami.net/?utm_source=efb_app&utm_medium=app&utm_content=point_view&utm_campaign=web_efp"},
            {"type": "E_FOOTBALL_POINT_SITE_FOR_COIN_MENU", "url": "https://efootball-point.konami.net/?utm_source=efb_app&utm_medium=app&utm_content=coin_view&utm_campaign=web_efp"},
            {"type": "CONNECTION_REPORT_VIEW", "url": "https://www.konami.com/efootball/_/page/online_match#antenna_icon"},
            {"type": "HELP_MOBILE_CONTROLLER", "url": "https://www.konami.com/efootball/_/page/mobile_controller"}
        ],
        "datapack_list": [
            {
                "filename": "data.pak",
                "datasize": 1234,
                "version": 1,
                "url": "http://example.com/data.pak"
            }
        ]
    }
    return response

@app.route("/auc/02_03_03/CmdGetCountryList.php", methods=["POST"])
@encrypt_response
def cmd_get_country_list():
    return get_json_response("GetCountryList.json")

@app.route("/auc/02_03_03/CmdCreateUser.php", methods=["POST"])
@encrypt_response
def cmd_create_user():
    response = {
        "msgid": "CMD_CREATE_USER",
        "rqid": 1661800258,
        "result": "NOERR",
        "user_id": 1885223288,
        "user_code": "ASDC592658275",
        "auth_code": "e1b18a57c1d365b283a4247db3f092ac34848751",
        "session_id": "8_ej07s0o1rlroshnnlebg8uald7",
        "svr_time": 1783007960
    }
    return response

@app.route("/auc/02_03_03/CmdGetMyclubEntryInfo.php", methods=["POST"])
@encrypt_response
def cmd_get_myclub_entry_info():
    response = build_entry_response("CMD_GET_MYCLUB_ENTRY_INFO", 1661800258)
    return response

@app.route("/auc/02_03_03/CmdCheckString.php", methods=["POST"])
@encrypt_response
def cmd_check_string():
    response = {
        "result": "NOERR",
        "rqid": 949774069,
        "msgid": "CMD_CHECK_STRING"
    }
    return response

@app.route("/auc/02_03_03/CmdSetMyclubEntryInfo.php", methods=["POST"])
@encrypt_response
def cmd_set_myclub_entry_info():
    return get_json_response("set_myclub_entry_info.json")

@app.route("/auc/02_03_03/CmdGetMyclubAchievementlist.php", methods=["POST"])
@encrypt_response
def cmd_get_myclub_achievement_list():
    response = {
      "msgid": "CMD_GET_MYCLUB_ACHIEVEMENT",
      "rqid": 123456789,
      "result": "NOERR",
      "achievement_list": [
        {
          "achievement_id": 1001,
          "present": {
            "present_id": 2001,
            "name": "Achievement 1",
            "title": "1",
            "body": "Good achievement",
            "entity_id": 3001,
            "present_type": "ITEM",
            "date": 1750000000,
            "count": 1,
            "agent_info": {
              "agent_id": 0,
              "name": "",
              "name_short": "",
              "name_short10": "",
              "skill_category": "",
              "skill_id": 0,
              "grade": 0,
              "count": 0,
              "type": "",
              "rate": {
                "rate_table": [100, 0, 0]
              },
              "target_level": 0,
              "multiple_count": 0,
              "image_file_name": "",
              "expiration_date": 0,
              "sell_gp": 0,
              "is_box_agent": "NO"
            },
            "item_info": {
              "item_grade": 1,
              "item_effect": 50,
              "item_type": "ENERGY"
            },
            "coupon_info": {
              "icon_name1": "",
              "icon_name2": "",
              "icon_name3": "",
              "view_image_name": "",
              "expiration_date": 0,
              "effective_time": 0,
              "limit_time_sec": 0,
              "serial": 0,
              "code": "",
              "name": "",
              "start_date": 0,
              "time_zone_offset": "+09:00",
              "time_zone": "JST",
              "url": ""
            },
            "source_id": "ACHIEVEMENT_01",
            "source_value": 10,
            "recv_term": 0
          },
          "present_type": "ITEM",
          "present_count": 1,
          "is_clear": "YES",
          "is_received": "NO",
          "achievement_num": 1,
          "achievement_need_num": 1,
          "level": 1,
          "complete_level": 1
        }
      ],
      "achievement_list_num": 1,
      "completeded_achievement_id_bit_array": [1, 0, 0],
      "displayed_tutorial_achievement_id_bit_array": 0
    }
    return response

@app.route("/auc/02_03_03/CmdGetProductList.php", methods=["POST"])
@encrypt_response
def cmd_get_product_list():
    return get_json_response("get_product_list.json")

@app.route("/auc/02_03_03/CmdGetMyclubMainmenuInfo.php", methods=["POST"])
@encrypt_response
def cmd_get_myclub_mainmenu_info():
    return get_json_response("get_myclub_mainmenu_info.json")

@app.route("/auc/02_03_03/CmdGetMyclubCoachContractNorma.php", methods=["POST"])
@encrypt_response
def cmd_get_myclub_coach_contract_norma():
    return get_json_response("get_myclub_coaches_norma.json")

@app.route("/auc/02_03_03/CmdSetMyclubTutorialAchievementInfo.php", methods=["POST"])
@encrypt_response
def cmd_set_myclub_tutorial_achievement_info():
    response = {
        "result": "NOERR",
        "rqid": 949774069,
        "msgid": "CMD_SET_MYCLUB_TUTORIAL_ACHIEVEMENT_INFO"
    }
    return response

@app.route("/auc/02_03_03/CmdGetMyclubCommentaryInfo.php", methods=["POST"])
@encrypt_response
def cmd_get_myclub_commentary_info():
    return get_json_response("get_myclub_commentary_info.json")

@app.route("/auc/02_03_03/CmdLogin.php", methods=["POST"])
@encrypt_response
def cmd_login():
    response = get_json_response("CmdLogin.json")

    if "rqid" in g.unpacked:
        response["rqid"] = g.unpacked["rqid"]

    return response

@app.route("/auc/02_03_03/CmdSetUserUpdateInfo.php", methods=["POST"])
@encrypt_response
def cmd_set_user_update_info():
    response = get_json_response("set_user_update_info.json")

    # Oyunun gönderdiği rqid değerini dinamik olarak eşitleyelim ki eşleşme hatası vermesin
    if hasattr(g, "unpacked") and g.unpacked and "rqid" in g.unpacked:
        response["rqid"] = g.unpacked["rqid"]

    return response

@app.route("/auc/02_03_03/CmdGetMyclubAgentList.php", methods=["POST"])
@encrypt_response
def cmd_get_myclub_agent_list():
    response = get_json_response("CmdGetMyclubAgentlist.json")

    # İstekteki rqid'yi dönen yanıta senkronize ediyoruz
    if hasattr(g, "unpacked") and g.unpacked and "rqid" in g.unpacked:
        response["rqid"] = g.unpacked["rqid"]

    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080, ssl_context="adhoc")