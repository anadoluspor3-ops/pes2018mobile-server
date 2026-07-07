def _make_coach(coach_id):
    """Return a dict matching the coach object structure."""
    concept = {
        "transition": 1,
        "build_up": 2,
        "attacking_area": 3,
        "mobility": 4,
        "defence_type": 5,
        "press_rule": 6,
        "first_df": 7,
        "passsupport_dist": 8,
        "offence_num": 9,
        "defence_line": 10,
        "defence_compact": 11,
        "defence_num": 12
    }
    return {
        "coach_id": coach_id,
        "contract_term": 10,
        "offensive_main_concept": concept,
        "defensive_main_concept": concept,
        "formation_data": "4-3-3",
        "gp": 500,                          # s1__2 = "gp"
        "pes_point": 100,
        "is_locked": "NO",
        "overall": 75,
        "management": 80,
        "adaptability": 70,
        "adaptability_rate": 60,
        "sell_gp": 200,
        "contract_gp": 300,
        "contract_pes_point": 50,
        "current_point_division": 0,
        "current_point_sim": 0,
        "current_point_vscom": 0,
        "is_use_variable_formation": "NO",
        "is_coach_texture_use": "NO",
        "norma_point_division": 0,
        "norma_point_sim": 0,
        "norma_point_vscom": 0
    }

def _make_gameplayer(gp_id):
    """Return a dict matching the gameplayer object structure."""
    concept = {
        "transition_counter": 50,
        "transition_possession": 60,
        "build_up_long": 70,
        "build_up_short": 65,
        "attacking_area_side": 80,
        "attacking_area_center": 75,
        "mobility_fix": 55,
        "mobility_float": 45,
        "defence_type_forecheck": 90,
        "defence_type_retreat": 85,
        "press_rule_net_defence": 40,
        "press_rule_seal_off": 35,
        "first_df_aggressive": 60,
        "first_df_safety": 70
    }
    return {
        "gameplayer_id": {
            "id": gp_id,                   # s1__0 = "id"
            "serial": 12345678901234
        },
        "games": 10,
        "goal": 5,
        "assist": 3,
        "yellow_card": 1,
        "red_card": 0,
        "injury": {
            "part": 0,
            "symptom": 0,
            "level": 0,
            "level_no_self_conscious": 0,
            "mcount_left": 0
        },
        "tiredness": 0,
        "contract_term": 15,
        "gameplayer_cost": 1000,
        "rating": 80,
        "concept": concept,
        "default_concept": concept,
        "is_rental": "NO",
        "sell_gp": 300,
        "contract_gp": 400,
        "contract_pes_point": 60,
        "uniform_number": 10,
        "level_info": {
            "level": 1,
            "level_limit": 50,
            "level_limit_max": 99,
            "exp_total": 0,
            "exp_current_level": 0,
            "exp_to_next_level": 100,
            "contract_gp": 200,
            "contract_coin": 0,
            "sell_gp": 100
        },
        "is_lock": "NO",
        "event_point": 0,
        "play_style": "Goal Poacher",
        "initial_base_team_id": 1
    }

def _make_item():
    """Return a dict matching the item object structure."""
    return {
        "item_type": "EnergyRecovery",
        "count": 5,
        "pes_point_price": 100,
        "grade": 1,
        "effect": 10
    }

def _make_squad(squad_id):
    """Return a dict matching the squad object structure."""
    return {
        "squad_id": squad_id,
        "name": "Main Squad",
        "member_list": [
            {
                "gameplayer_id": {"id": 101, "serial": 111},
                "uniform_number": 1,
                "player_level": 10
            }
        ],
        "member_num": 1,
        "is_entry_compe": "NO",
        "coach_id_list": [1],
        "gameplan_data_size": 0,
        "gameplan_data": "",               # binary blob, empty for now
        "tactics_kind": "OFFENSIVE"
    }



def build_entry_response(msgid, rqid):
    return {
        # Top‑level echoed fields
        "msgid": msgid,                    # echo from request
        "rqid": rqid,                      # echo from request
        "errcode": "NOERR",                # string, "NOERR" for success
        "result": "NOERR",                 # string

        # ------------------------------------------------------------
        # entry_info – main player/team data
        # ------------------------------------------------------------
        "entry_info": {
            "gp": 999999,                  # s1_ = "gp"
            "pes_point": 5000,
            "team_name": "MyTeam",
            "team_name_short": "MYT",
            "base_team_id": 123,
            "base_team_license": "licensed",
            "national": 0,                 # 0 or 1?
            "user_name": "PlayerName",
            "home_town_name": "Tokyo",
            "home_stadium_name": "Konami Stadium",
            "extend_team_player_max_gp": 500,
            "extend_team_player_max_pes_point": 1000,
            "extend_team_scout_max_gp": 200,
            "extend_team_scout_max_pes_point": 500,

            "team_energy_info": [
                {
                    "kind": "STAMINA",
                    "max_gp": 100,
                    "max_pes_point": 50
                }
            ],
            "total_get_player_num": 1000,
            "scout_agent_max": 10,

            # ------------------------------------------------------------
            # Lists of coaches, players, items, squads
            # ------------------------------------------------------------
            "coach_list": [_make_coach(1)],          # example coach
            "coach_list_num": 1,
            "gameplayer_list": [_make_gameplayer(1)],# example player
            "gameplayer_list_num": 1,
            "gameplayer_list_max": 900,
            "item_list": [_make_item()],             # example item
            "item_list_num": 0,
            "squad_list": [_make_squad(1)],          # example squad
            "squad_num": 1,
            "main_squad_id": 1,
            "default_coach_list": [_make_coach(2)],  # another coach
            "default_coach_list_num": 1,

            # ------------------------------------------------------------
            # game_option_info – nested settings
            # ------------------------------------------------------------
            "game_option_info": {
                "language": "en",
                "display_info": {
                    "radar_disp": "ON",
                    "player_name_box_flag": "ON",
                    "radar_icon_color_home": 0xFF0000,
                    "radar_icon_color_away": 0x0000FF,
                    "power_bar_flag": "ON",
                    "cursor_disp_flag": "ON",
                    "stamina_bar_flag": "ON",
                    "time_score_flag": "ON",
                    "tactical_plan_flag": "ON",
                    "com_name_disp_flag": "ON",
                    "setplay_guide_flag": "ON"
                },
                "sound_info": {
                    "menu_effect_volume": 80,
                    "bgm_volume": 70,
                    "commentary_volume": 90,
                    "env_volume": 60,
                    "device_music_flag": "OFF"
                },
                "push_notification_info": {
                    "information_flag": "ON",
                    "team_stamina_flag": "ON",
                    "final_round_flag": "OFF",
                    "favorite_scout_flag": "ON"
                }
            },

            # ------------------------------------------------------------
            # Other top‑level entry_info fields
            # ------------------------------------------------------------
            "energy_recovery_time": 3600,
            "online_rating": 800,
            "secure_match_level": "low"
        }
    }
