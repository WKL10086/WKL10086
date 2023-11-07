Main Game Flow

```mermaid
graph TD
start[START] --> new_issue[Receive new issue start with 'wkldle-']
new_issue --> guess_or_init{Is issue a guess or an init?}
guess_or_init --> |Init| new_word[Generate a new word]
new_word --> save_new_word[Update ans.json with that new word]
save_new_word --> init_readme[Init repo README.md]
init_readme --> close_issue_init[Close issue with a init finish message]
guess_or_init --> |Guess| is_finished{Is game finished?}
is_finished --> |Yes| close_issue_finish[Close issue with a finish message]
is_finished --> |No| is_valid{Is guess valid?}
is_valid --> |No| update_log_invalid[Update log.json with invalid status]
update_log_invalid --> close_issue_invalid[Close issue with a invalid guess message]
is_valid --> |Yes| is_correct{Is guess correct?}
is_correct --> |Yes| update_game_state_correct[Update game state]
update_game_state_correct --> update_log_correct[Update log.json with valid and correct status]
update_log_correct --> save_log[Save log to prev_log folder with answer]
save_log --> update_readme_correct[Update repo README.md with the correct answer]
update_readme_correct --> init_log[Init log.json]
init_log --> close_issue_correct[Close issue with a correct guess message]
is_correct --> |No| update_game_state_incorrect[Update game state]
update_game_state_incorrect --> update_log_incorrect[Update log.json with valid and incorrect status]
update_log_incorrect --> is_last_try{Is this the last try?}
is_last_try --> |Yes| update_readme_finish[Update repo README.md with the incorrect guess and the correct answer]
update_readme_finish --> close_issue_incorrect[Close issue with a incorrect guess message]
is_last_try --> |No| update_readme_incorrect[Update repo README.md with the incorrect guess]
update_readme_incorrect --> close_issue_incorrect
```
