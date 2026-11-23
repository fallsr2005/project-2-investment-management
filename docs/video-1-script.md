AI used: ChatGPT/Codex assisted with code, tests, source checks, documentation, and this presentation draft. I am responsible for reviewing the analysis and owning the decision.

Education only — not investment advice.

# Video 1 — system evolution and checked AI output

This is a rehearsal script and screen-action guide, **not an actual transcript**. Maximum **3:00**; aim for **2:40–2:50**. Timing estimates are not a measured recording. Rehearse until you can explain the evidence naturally; adjust any personal reflection to match your actual experience. Your professor's Project 1 feedback emphasized speaking from the tool and submitting what was actually said.

Video 1 answers: **How did the system and your thinking change, and which AI output did you check?** It does not need a full code walkthrough or every project detail. The [course architecture](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md) requires a small webcam view unless accommodated. Project 2 has no submitted Editions A/B.

## Prepare the screen before recording

Open these browser tabs in this order. These are existing artifacts; no new app feature or protected experiment is needed.

1. **App:** [localhost:8501](http://localhost:8501). Set all 59 returns, SGOV minimum 10%, implementation cost 0.00, ACWI adjustment 0.00, and no replacement CSV. Confirm 70% SGOV / 30% ACWI, 6.02% net estimate, 4.56% volatility. Keep the title and base table visible; adjust browser zoom for legibility if needed.
2. **Earlier AI-assisted memo:** [original memo at initial commit](https://github.com/fallsr2005/project-2-investment-management/blob/bea2f9e98293df21726640d860fe600bb7fa517d/docs/decision-memo.md). Scroll to “Recommendation and committee ask,” showing the 65–75% SGOV operating-range sentence. This is historical wording, not the final recommendation.
3. **Corrected memo:** [current decision memo](https://github.com/fallsr2005/project-2-investment-management/blob/main/docs/decision-memo.md). Position the paragraph beginning “Within the original” so the candidate band and feasible subset are visible.
4. **Recorded changed-run allocation:** [after portfolio screenshot](https://github.com/fallsr2005/project-2-investment-management/blob/main/docs/evidence/acwi-minus-3pp/after-portfolio.png). Fit the image so -3.00, 50/50 weights, 6.01%, and 7.50% can be read.
5. **Recorded changed-run decision:** [after decision screenshot](https://github.com/fallsr2005/project-2-investment-management/blob/main/docs/evidence/acwi-minus-3pp/after-decision.png). Show REVIEW and the 20.00-point change. Label it verbally as the recorded experiment, not a new live run.

Also open a **PowerShell window** for one transparent hand check. Type this expression, leaving it ready to execute during the relevant segment:

```powershell
0.75 * 3.78 + 0.25 * 11.25
```

It should display **5.6475**, in percent units because the inputs are percentages. Rounded, that is **5.65%**, below 6%. These are the app's rounded SGOV/ACWI return inputs, not a new optimizer run. If you want to see their source beforehand, scroll the app to “Historical inputs”; return to the base table before starting. This is the check you demonstrate, so understand it and actually show its result rather than claiming a check you have not performed.

If the app is closed, use the README's existing launch command from the project directory:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Timed script and exact actions

Say the quoted text; do not read the action labels aloud. The timestamps are rehearsal targets. Keep normal pauses and stop before 3:00.

### 0:00–0:20 — opening disclosures

**Screen:** tab 1, app title and base allocation. Begin with your microphone and small webcam view active.

> I used ChatGPT and Codex to help with code, tests, source checks, and this presentation draft. I am responsible for the analysis and decision. This is education only, not investment advice.

### 0:20–0:45 — how the system and thinking changed

**Screen:** stay in the app; point to the two baseline rows and constrained portfolio. Scroll slightly if needed. Leave the controls unchanged.

> My project developed from the lab's baseline calculations into an app that compares two baselines with a constrained portfolio. Initially, I focused on whether the portfolio passed. Now I separate numerical feasibility from whether the committee should use it. That change came from course work, AI-assisted review, and my own stress exercise.

### 0:45–1:20 — show one AI-assisted output and check it

**Screen:** switch to tab 2 and point to the earlier 65–75% SGOV operating range. Then switch to PowerShell, press Enter on the prepared calculation, and point to **5.6475**. Keep the calculation visible while explaining it.

> This earlier AI-assisted memo suggested a sixty-five to seventy-five percent SGOV operating range. I qualified that suggestion by checking the seventy-five percent endpoint. With the app's rounded return inputs, seventy-five percent times three-point-seven-eight, plus twenty-five percent times eleven-point-two-five, equals about five-point-six-five percent. That misses the six-percent hurdle.

### 1:20–1:45 — disposition: qualified and clarified

**Screen:** return to the browser and select tab 3, the current memo. Point to the **65–70% SGOV / 30–35% ACWI** feasible subset.

> The corrected memo separates the candidate review band from the feasible range. Under the base assumptions, the feasible grid candidates within that band are sixty-five to seventy percent SGOV, paired with thirty to thirty-five percent ACWI. Every candidate still needs checking after costs or input changes.

### 1:45–2:25 — your experiment and its effect on judgment

**Screen:** show tab 4, the saved after-portfolio screenshot. Point to -3.00, 50/50, 6.01%, and 7.50%. At “passed the mandate,” point to PASS. Then select tab 5 and point to **REVIEW** and **20.00 percentage points**. Do not change the live app's controls for this segment.

> For my recorded experiment, I reduced ACWI's annual-return estimate by three percentage points. I wrote the prediction myself; the later formatting and Git assistance are disclosed. The actual allocation became fifty percent SGOV and fifty percent ACWI. Estimated net return was six-point-zero-one percent, and volatility rose to seven-point-five percent. The portfolio passed the mandate, but its twenty-point weight change and allocation-band breach triggered REVIEW.

### 2:25–2:50 — what you now conclude

**Screen:** return to tab 1's base allocation. Point to 70% SGOV / 30% ACWI. Finish, then stop recording.

> This changed my judgment: passing the return hurdle is not enough. I retained a conditional three-month process pilot with monthly reviews, and I require committee reassessment before using the stressed allocation. The saved restoration evidence returned to the base seventy-thirty mix. Historical estimates and frozen source snapshots limit what this process can establish.

## Record with screen, voice, and webcam

Use **Microsoft Clipchamp**: search Start for Clipchamp, or open [the web editor](https://app.clipchamp.com/) in Edge/Chrome. Sign in if required.

1. Create a video project; choose **Record & create → Screen & camera**.
2. Allow camera/microphone access; select your microphone.
3. Choose **Entire screen** so browser/PowerShell switches are captured. Computer sound is unnecessary; your microphone must record your voice.
4. First make a 10-second trial, then play it back to confirm voice, screen, and webcam.
5. Record the rehearsed sequence; stop and choose **Save and edit**.
6. Keep webcam and screen aligned in the timeline. Resize the camera overlay so it covers no required numbers.
7. Trim dead time and export **1080p MP4**. Play the exported file; confirm readable evidence, audible voice, both opening disclosures, webcam, and duration ≤3:00.

[Microsoft recording instructions](https://support.microsoft.com/en-us/clipchamp/how-to-make-a-screen-recording), [MP4 export instructions](https://support.microsoft.com/en-us/clipchamp/exporting-and-saving-a-video-in-clipchamp).

Keep rehearsal notes off the shared screen, using paper, a phone, or another screen. Save the webcam recording in your personal Videos folder outside the course repository; it contains personal imagery. The submission uses a YouTube link, not a committed video file. You do not need music, titles, slides, or other production extras.

## Upload and create the actual transcript

1. In [YouTube Studio](https://studio.youtube.com/), select **Create → Upload videos** and choose the exported MP4. Suggested title: **Project 2 — Video 1: System Evolution and AI Check**.
2. Set video language to English and answer the audience setting accurately. Choose **Unlisted**, finish the upload, and wait for processing. Anyone with the unlisted link can view it; test the link logged out.
3. In **Subtitles**, open this video and review its captions. For automatic captions, use **Duplicate and edit** where shown. Correct finance terms, tickers and numbers; publish the corrected track. Auto-captions can take time; if unavailable, enter an actual transcript and use YouTube's timing tools.
4. Download the corrected captions or copy their text. Compare it with the actual exported recording, not this draft. Send the caption/transcript text and YouTube URL back for review.
5. After review, replace `docs/transcript-video-1.txt` with the actual spoken transcript and update Video 1's manifest URL, duration, real timestamp index, and access result. Do not use these rehearsal timestamps as observed timestamps.

[YouTube upload instructions](https://support.google.com/youtube/answer/57407?hl=en), [visibility](https://support.google.com/youtube/answer/157177?hl=en), [caption editing/download](https://support.google.com/youtube/answer/2734705?hl=en), [adding captions](https://support.google.com/youtube/answer/2734796?hl=en).

Correct captions to match what you actually said. If the speech itself contains a material financial error, fix the recording before finalizing; do not silently rewrite the transcript to claim a different statement. We will check this Video 1 recording/transcript before preparing Video 2. Completing Video 1 does not complete the other two videos or final package.
