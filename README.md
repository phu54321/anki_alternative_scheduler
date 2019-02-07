# anki_alternative_scheduler
Alternative scheduler for anki.

Build your scheduler here.

## Using your own revlog file.

1. Run anki's console with `Ctrl+:`
2.  On a console window, paste the code below.
    ```py
    import os

    with open(os.path.expanduser('~/Desktop/revlog.csv'), 'w') as f:
      f.write('id,cid,usn,ease,ivl,lastIvl,factor,time,type\n')
      for row in mw.col.db.execute('select * from revlog'):
        f.write(str(row)[1:-1])
        f.write('\n')
    ```
3. Type `Ctrl+enter`
4. File called `revlog.csv` would be at your desktop. Upload that file.

>  For privary-concerned: What revlog.txt does.
> 
> `revlog.csv` has these as a content, as indicated [here](https://github.com/ankidroid/Anki-Android/wiki/Database-Structure).
> 
> - id: Time you did the review
> - cid: Time you made the card. Unique for each card.
> - usn: Some metadata used for AnkiWeb sync. It tells which data is newer, on web or on your PC.
> - ease: What button you pressed. Again/Hard/Normal/Easy
> - ivl: Next interval of the card. (You should wait for interval time to study the card again)
> - lastIvl: Previous interval of the card
> - factor: SM-2 algorithm related thing
> - time: Time spent for each review.
> - type: Type of review (new card? learn? relearn? cram?)
> 
> There aren't anything privacy-related I think. It may reveal the time you do study the most, the time you create the card the most. That's all I think.