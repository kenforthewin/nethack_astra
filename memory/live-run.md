# Live run 1 — 2026-09-06

## USER STOP OVERRIDE — 2026-09-08

User explicitly said "lets stop there" after death. OBS verified OFF.
Postmortem finalized; Hardfought at logged-in lobby, no saved character and NO
new game started. Do not act on the old keep-playing instructions below.
Read EVIDENCE.md: new stream decision/command feed, private audit ledger,
continuous observable-transcript watcher, terminal pipe and fail-closed input.
Archive directory records/20260908T171811Z-b726582e. Three game-session ttyrecs
and final dumplog downloaded with checksums. OBS local recording was OFF and
Twitch VOD remains unverified. Resume only when Kenny explicitly asks.

## FINAL: DEAD by sliming on D51, T33302, 2026-09-08

Invocation completed, maximum dungeon level52; Sanctum never entered.
Hero died11,29 D51. Baluchitherium killed33292; green slime killed33295-ish,
but sliming began during an unsafe 24-key movement batch near known slime.
At33297 Slime status recognized; attempted zh. but h was EMPTY, and the spare
period spent time. Then removing robe/GDSM consumed the remaining turns.
CRITICAL CORRECTION verified zap.c lines2249-2255: SELF-ZAPPING POLYMORPH
IGNORES MAGIC RESISTANCE. Could have used zY. immediately in GDSM (gray dragon)
without removing armor; charged Y1:6 remained. Do not repeat this false premise.
Source: https://raw.githubusercontent.com/NetHack/NetHack/NetHack-3.6.7_Released/src/zap.c
Lessons: no blind movement batches near dangerous monsters; stop on fresh
messages/status changes; VERIFY usable fire charges before Gehennom; maintain
uncursing reserve; do not wear levitation during Wizard fight if avoidable.
This run is OVER. All maps, inventory appearances below are run1 ONLY.
User said keep playing until stopped; continuing streaming into new dwarf Valk.

## Current checkpoint T33286 — invocation done, curse recovery

D51 southwest maze, hero21,29 before next westward movement; HP148/165, XL18,
AC-19, Co19, levitating g, blindfold O OFF. Original Wizard stole Orb33172,
Bell33186, Book33235. First clone killed D52 44,23 T33205, FAKE amulet only.
Original plus second clone now D51, usually upstairs26,13; original visits hero.
CURSED GLOVES u prevent removing still-uncursed levitation ring g. Cannot
descend or pick up ground items. CAN ascend. Target D50 magic trap19,13 to
uncurse worn gear, then recover Orb. Invocation D52 22,23 succeeded33169;
new stairs to Sanctum53 unvisited. Candelabrum left D51 30,27 T33238.
Full healing K consumed33253: maxHP165. Blessed EXTRAHEALING J MAIN ready.
Unc gainability R consumed33257 Co19; cursed S gainability bagged33258.
BOH82 direct items, oilskin20 plus ordinary sack2 now both DIRECT in BOH.
No holy water, remove curse, charging or wishing remain. Marker1:0 empty.
X teleport0:4; W teleport4 hero uses; e lightning2 uses; m death1:0 empty.
Last C-ration E rotten then finished33265. Food remains BOH; main lizards/tin.
Orb absent means NO half damage; retrieve BOH luckstone when safe.
Green slime and baluchitherium southwest corridor; Wizard teleports here.
Route planner scripts/route.py read-only proposals excludes monsters; no route
may mean a monster blocks the only exit. Current southwest corridor deadend
at21,29 exits WEST through13,29 then13,28. Do not try north21,29 (rock).
session keys --settle 3 supports longer animation wait. OBS46:20:34 healthy.
Keep playing/streaming until user says stop. Older checkpoints below stale.

THIS SUPERSEDES the shakedown character in session.md.
User explicitly requested Twitch streaming and a NEW dwarven Valkyrie.
Shakedown character retired via #quit. Fresh character started normally.

Stream active since 18:44:46 UTC. USER OVERRIDE: "dont stop at 30 mins, keep going
until i say to stop". The automatic cutoff process in tmux session `broadcast`
was interrupted, leaving OBS streaming. No deadline now. Keep playing until
the user says stop; then save and run `node scripts/obs.mjs stop`, verify stopped.
Do not end the assistant turn and leave an unattended active broadcast.
The old stopAt in .runtime/broadcast.json is obsolete. `status` includes stats.
At 18:54 UTC: 9m39s live, zero skipped frames, zero congestion, no reconnecting.

Character: CodexDelver, lawful female dwarven Valkyrie, normal scoring game.
CRITICAL LATEST T33188 D52hero39,15 HP133 AC-19 XP1319353 OOFF gON CANNOTREMOVELEV because uGLOVESCURSED (ringgstillUNC CstillBLESSED inventory33181); remove menu[IO] duegloves. WIZARD RESURRECTED33170 atVS immediatelyafterSUCCESSFULINVOCATION33169! **STOLE ORBOFFATE D33172 and BELLF33186**, NOW BOTH NOTMAIN; mustreclaimOrb. **DOUBLE TROUBLE33185 TWO WIZARDS alive**. BothteleUP45,22heal ifdist>8 sooccupyUPtoblockhealing. HPmax161 main2WIZhardhitsbutnotcritical. MainmDEATH1:0empty, eLIGHTNINGNOWTWOHEROUSES S39,15T33188bothhitWizard. WteleNOWTHREEHEROUSES: self70,17→41,13T33183;S39,15T33187teleportedelf; initial? W1self33183, W2S33187 soTWO actually. XTELE1selfVS22,23→70,17T33174 now0:7. WizardstoleOrb mainwarning+halfphysical+halfspellGONEuntilreclaim! Excal3blessedstillmain,MRQblessed unchanged.
INVOCATION DONE33169 VS22,23nowDOWNtoSANCTUM53. H BLESSED RC CONSUMED33168 (calledremove curse/EIRIS SAZUN IDISI), noRCreserves/wish/holywater/marker. Candeli7UNLITagain33173. BookrIDnowuncursedpostRC maybeWizcurseslater. NEWMOAT x17..27 y19..27 outer2ring, FIRETRAPS8aroundVS x21..23 y22..24; LEVdoesnotavoidfire. VSsummons33174 included3MINDFLAYERS north/south, D/H/Y/w/@; teleescapedXself. Wizardfollowed, 6Excalhitsbutretreatshealing. Wizard2 summons33188 AngelA40,15hostile? notattackingyet. CurrentWizard39,16(S) andotherhealingUP45,22; needscreenafterspellanim. NAGA39,16previousprobablyshifterSHRIEKER39,15killed33186. DISENCHANTER Rwas39,21, avoidmelee.
CURSEGLOVESproblem potentialsolution MAGIC TRAP D50at19,13; canASCENDstairswhileLEV (verify), MAGICtrap1/20uncurseswornitems(source trap.c domagictrap fate20 SCR_REMOVE_CURSE uncursed), but1/30explodes and45%spawnsmonsters. NOnearerknownmagic(D51noneknown;D52noneknown). Couldusepolyselfgraydragon afterremoveRobe topreserve+5 toslipgloves butlessdesirable; polypilingcan'tpickupfloorwhilecursedLEV. NeedrecoverOrbfromWizardfirst. MainWtele2herouseunknowncharges; eLightning2herouse+monster1; zCold4herouseunknown. OBS45:57:41 healthy245skips0congestion.
LATEST approachingD52 T33138 D51hero55,27 midPOLYMRanimation, queuedresttoDOWN59,28 Rg>. ONE BLESSED REMOVE CURSE H(EIRIS SAZUN IDISI) BAGGED33005 unused. WISHGONE. BookrCURSEDnotread. PlanretrieveHATVS22,23D52 readtoUNCURSEALLmainthenai(light7candel) aF(Bell) rr(Book). Needverifybookeffect nointerveningcurse. MDEATHEMPTY1:0. MainzCOLD4uses/otherreservesunchanged. FullHP161AC-19 XP1319336. NOHUNGER lastNurse32472. D49LIEUTdead9,27T33030. QUANTUMnear27,15teleportedusto75,19T33066→44N2W2toDOWN71,17. D49centralB41,14stillintact bypassUNFIXED. D50MOUNTAINCENT near36,25dead33078XP+375; COCKATRICE52,26dead33086. BlindfoldusedacrossD50thenremovedD51. D51routecleanUP26,13→47,29T33130 thenDOWNbatchinprogress. AllinvocationitemsMAINexceptHscrollBOH83direct.
LATEST T33004 D48hero75,29 HP161 AC-19 XP1318522 gON OOFF. WREST WISH SUCCEEDED33004 kWAND TURNEDTODUST permanentlygone. Wished3BLESSEDRC butONLYONEGRANTED: H scroll EIRIS SAZUN IDISI=blessedREMOVE CURSE. NOTREAD! PlanBAGHuntilVS toavoidcurse/fire, retrieve/readwhenreadyinvoke; Bookr CURSEDbygeneration (makemon.c mongets explicitlysetsSPE_BOOK cursed); candelunknowncouldcursed bydemigod. Bookr MAIN. BellFmainuncursed, candel7unlitmain. nCREATEbagged32876. BOH82(afterwishremoved/nadded),83afterHstash. NoWISHleft/noholywater/nocharging/markerempty. DEATHm1:0 MAINempty. QGDSMnowBLESSED observedinventory32875. EverythingelseknownBUCunchanged includingBLESSEDBOH. Blackglow/malignantaura32866 demigodcurse maybeunknowngear.
Towerescaped: D40batdead32815. MIDDLEreturndeadGIANTZOMBIE+NURSEnear29,18T32838; 2hellpups27,19/20dead32846; ELFMUMMY27,23dead32849; ORCMUMMY30,23dead32858; LEATHERGOLEM35,26dead32861; FIRE ELEMENTAL36,24dead32866. ZOOshortreturn36,25N36,24NE37,23NE38,22NE39,21N39,20NE40,19N40,16 (peacefulgnomekingroamsblocks). MAGICTRAP47,16trigger32876 blinddeaf spawnedROCKTROLL47,16alive; escaped49,16S49,18SE50,19S50,24 W47,24N47,22W44,22S44,26W39,26down. NEWPIT50,23 LEVbypasses. Bottom36,22PgS36,26ice36,25MELTEDbutcrosssafe, eelsmissed. Allrouteportalunchanged; D48landed32931 theneastmaze at75,29T33004. Lastmeal32472 noHunger yet. OBS45:50:56 healthy245skips0congestion.
LATEST T32815 REALWIZTOP40 hero39,16 HP161 AC-19 XP1317087 Ch10 NOHUNGER gOFF OOFF aWIELD. WIZARD FIRSTKILL32809 at40,17 BOOKr(PAPYRUS) PICKED32813 with nCREATEscroll BOTH MAIN. mDEATH NOW1:0 EMPTY:6thS41,17 killedhellhound41,18 missedteleportedWizard;7thW41,17KILLEDWIZ. DEMIGODCLOCKNOWRUNS. Vampirebat38,16DEAD32815. MAINzCOLD FOURUSES latestE41,17freezerow17T32804 maybeempty. VladCOLDoldP ONEUSEW41,17T32804 nowBAGGED alongsideASMOd0herouse andPICKb. BOH82. BookBUCunknown, candel7ready Bell3ready. WISH1:0BOH NEVERWRESTED considernewdeathwand. NOHOLYWATER. LastmealNURSE46,16D41finished32472. INVISIBLEpermanent.
TOP FASTRETURN:39,16W35,16S35,17W30,17S30,19SE31,20LADDERdown→D41UP37,16. SECRET36,16FOUND32793 OPEN plus33,17+30,18 OPEN. Moatrow17x38..44ICE. SEAremain39,18/38,19/43,18/44,22/41,23/39,23 etc; VAMPLORDwolf41,20alive. ICEDEVIL35,25DEAD32614; MAGICTRAP35,25gaveCh+1; WHITED30,16DEAD32588;HEZROU48,25DEAD32671;TIGER47,24DEAD32675;3APES40,26/37,26/32,23DEAD32756/759/778. PeacefulFIREGIANTlowerleftavoid.
MIDDLE ZOOreturn stillcrowded: reverse recorded route. GLASSGOLEM36,22, BLUE DRAGON41,22, IRON?GOLEM40,21, FOURDEMONS36..38y18..19, COCKATRICES39..41y22..24, nursefollowedto31,24 +fireelementalto32,26. Deadcaptain36,23/energyvortex36,23/horse36,23/owlbear37,22/ettinmummy38,21/hellpup37,21/plainsC37,21/warhorse38,20/jabber39,18/redD41,18/trapper39,18/chickatrices40,18/orccap40,18. MAGICTRAP47,16 stillactive spawnedpurpleworm/nurse/jaguarallkilled32452; mustcrossreturn. Bottommoat36,25 ICE maymelt; activateLEV, quickS36,26 thenknownrouteportal50,26.
LATEST WIZTOPD40 T32574 hero31,20 LADDERDOWN HP161 XP1310852 AC-19 SATIATED gON OOFF aWIELD. Wizard41,20ASLEEP Bookstillnotobtained. HEZROU31,19DEAD32572 summonedICEDEVIL30,19nowfighting. WHITEDRAGON30,17approaches. OtherICEDEVIL35,25 (different),peacefulFIREGIANT32,24,demons47,20/53,25. Fishmoat38..44y17..23. Needreachmoat viaRANDOMSECRETroomdoor inoutermorgue walls36/46y16..24; staticmapyendor.des hasNO fixedentry! Ladder31,20→30,19→secret30,18→30,17→27,17→27,23→secret28,23→35,23 andsearchwall36,22..24, orothermorgueborder. Keepdeath2chargesWizard. MainzCOLDoneherouseN36,26BOTTOM32387. S EMPTY/Z DIG EMPTYtested32388 bothBAGGED32401alongwithpick. BOH82direct. NOinventorychangesexceptz1charge. MainLextrahealDESTROYEDold;BOHhealingunknownnew+blessedextrahealSAFE.
WIZBOTTOM42 LADDER36,22REACHED32400; MOATICE33..36,25 frozen,36,24wallPICKDUG32392. Toportal:36,22S36,26W32,26N32,25W27,25N27,19E30,19N30,16E49,16S49,21W45,21S45,26E50,26portal. Kraken/eelsremainwater;drowningignoresLEV. InnerVAMPLORD36,23DEAD32395;MOUNTAINC36,22DEAD32398;HORNEDDEVIL36,24DEAD32399. ARMOR? amulet36,22undercentaurcorpseLEFT. RgfloorautolookMENU thenSPACEbefore<. MainS0:0/Zempty andpickbaggedatladder. S5thlastcharge32383, zFIRSTcharge32387.
WIZMIDDLE41 DOWN39,26↔bottomUP36,22; UP37,16↔TOPDOWN31,20. FAST DOWN→UP discovered32568:39,26E44,26N44,22throughsecret44,23E47,22S47,24throughsecret47,23E50,24N50,19throughsecret50,20NW49,18N49,16throughsecret49,17W40,16S40,18throughsecret40,17SW39,19SW38,20SW37,21S37,22SW36,23S36,26throughsecret36,25W31,26N31,24throughsecret31,25W27,24N27,18throughsecret27,22E29,18S29,20throughsecret29,19E32,20N32,16throughsecret32,19E37,16throughsecret33,16. ALLDOORSOPEN. MustcrossZOO34..42y18..24. Numerousmonstersstillalive canfollowoutside. NoTELE/DIGentirelevel. MAGIC TRAP47,16 triggeredblinddeaf+spawn32440ish; MUSTCROSSAGAINonewidthcorridor. NURSE46,16DEAD32451ATE32472 latestmealSATIATED. PURPLEWORM47,16DEAD32446, JAGUAR48,16DEAD32452. ZooDEADorc-captain40,18/grayunicorn40,18(shifter)/2chickatrice40,18/trapper39,18/redD41,18T32492/JABBER39,18T32501/warhorse38,20/quiveringblob37,21/ettinmummy38,21/HELLPUP37,21/PLAINSC37,21/OWLBEAR37,22/HORSE36,23/CAPTAIN36,23T32519/ENERGYVORTEX36,23T32520. GearcorpsesLEFT. ALIVE NURSE37,23followslast31,24warning4T32547;FIRELEMENTAL36,24follows;GIANTZOMBIE37,20;ELFMUMMY38,21;GLASSGOLEM36,22;BLUEDRAGON41,22;MANYCOCKATRICE/PYROeast;4demons36..38y18..19sleeping. Nochargesusedmiddle. LatestOBS45:29:19healthy245skips0congestion~4min.
LATEST REAL WIZARD TOWER BOTTOM D42 T32386 hero36,26 HP161 XP1305190 AC-19 gON OON (willRO) aWIELD INVIS NOHUNGER lastmeal31980. Entered D48PORTAL39,21 T32303→D42PORTAL50,26. LADDER36,22 NOTREACHED; moat approach south36,26→36,25water→wall36,24→floor36,23→ladder36,22. MAIN S COLD NOW0:0 fifthlastcharge E32,25T32383 froze33..35,25 only. zCOLDfresh main, Zdig7usesmaybe1remain. PICK bBLESSED BAGGED32231. BOH80 direct includesNEWUNKNOWNHEALINGoldk ICEDEVIL47,16picked32348bag32349. Hempty/Jcreate/Kcurslow/Vmm bagged32012..15, ZEROHOLYWATER, MAINLextrahealDESTROYED32107. mDEATH1:2 unchanged. WizardASLEEPD40BOOKNOTYET. Bell+candel7ready. VS52 22,23 physicallysecured31933. LatestOBS45:26:10 healthy245skips0congestion.
TOWERBOTTOM routePORTAL50,26W45,26N45,21E49,21N49,16 throughOPENDOORS49,20/49,17W30,16 viaOPENDOOR41,16S30,19W27,19 viaOPENDOOR28,19S27,25E32,25 viaOPENDOOR31,25SE33,26E36,26. OuterwallNONDIG innerislanddiggable. Sea monstersDROWNIGNORESLEVITATION: ifwrapped freezeMONSTERwater tile or RgONLYoverSOLIDGROUND. Tele32386fish34,19/33,21/33,22/33,23; &32,23 unknown demon approaches; B35,22 andC36,22 insideisland; bees42..43y21..25 +DRAGON42,26+OGRE43,26 enclosedhive. OutsideblackD55,28 irrelevant. DEADmarilith48,26T32305/vamplord49,25T32308/redD48,26T32313/grayD48,25T32318/ogreking49,21T32327/wraith49,19T32330/scorpion49,21T32333/icedevil47,16T32345/largemimic44,16T32353/succubus38,16T32362/pyrolisk27,23T32375. Corpses/gearLEFT excepticehealingbagged. OgreMMwand49,21left3monsteruses. Source yendor.des bottomoffset25,15;ladder36,22. Middle UP37,16/DOWN39,26. TopDOWN31,20 WIZARD41,20ASLEEPBOOK.
D48return disench61,20DEAD32265 accidentalmelee noAC/Excaldrain verifieda+3T32266. Portal39,21 armorLEFT. ReturnDOWN77,24routeinoldermemory: portalE43,21S43,22E45,22N45,21E47,21N47,19W45,19N45,17E49,17N49,13E51,13S51,17E53,17N53,13E55,13S55,17E57,17N57,15E59,15S59,17E63,17S63,19W61,19S61,21E63,21S63,23W61,23S61,25E63,25S63,27E67,27N67,25E74,25SE75,26S75,29E77,29N77,24DOWN. D49NEWB41,14blocksoldbypass needbreakorDIG42,13 whenreturn.
LATEST D49T32230hero23,29 HP161 XP1301017 SATIATED gON OOFF aWIELD. Next66aysbRg<to48DOWN77,24. MAINL EXTRAHEALING DESTROYEDPYROLISKGAZE D50T32107 (blessedBOHpstillSAFE). MAINpSTRIKE SIXHEROUSES latestD49S43,13destroyedNEWB43,14T32166; pprobablyemptybutnottested. MAINPICK bblessed carrieduntilnextstash. BOH79afterpickstashed (78whileout); includesH EMPTY/J CREATE0:3/K CURSEDSLOW0:1/V MM0:2. BellFstillmaincantbag. HOLYWATERZERO. MainmDEATH1:2 andOrb0:0unchanged.
D50FAST DOWN→UP:69,21SW68,22W66,22S66,26W44,26NW43,25W34,25S34,26UP. PICKSHORTCUTS65,26 /56,26 /38,25. B43,26bypassrow25. FIRE30,26notonroute. REDDRAGON70,20DEAD32077;REDNAGA64,26DEAD32087;XAN38,25DEAD32109;MOUNTAINCENTAURnear36,24probablydead32112XP+189duringblindmoves. PYROLISK41,19alive gazeDESTROYEDLextraheal32107; POuntilUP49thenROcured. Otherc42,20/63,23unknown. UP49arrived32114, thenall50left.
D49NEWPICKSHORTCUT64,25 links65,25↔63,25 avoidswholeSEboulderloop. BALUCH45,13DEAD32157no corpse(probablyshifter); OCHREJELLY40,13DEAD32171no corpse(probablyshifter). STORMGIANTS numerousALIVE throwBs andLIGHTNINGwands; newB43,14STRIKEBROKEN32166, B41,13pickedbygiantandTHROWNTO41,14nowBLOCKSOLDRETURN DIAGneedbreakonnextpass! CanalsoDIG42,13to41,13nowclear. HeroescapedwestthenknownrouteSWtoUP. New2warning18,23 and1warning20,20 unIDnearUPpotentialfollowers. STORMGIANT42,15alive;elflord36,15alive;manyshiftersmiddleincldragons/minotpossibilities. LastOBS45:07:36~5min.
LATEST D50T32078 hero69,21 DOWN69,21↔D51UP26,13 FOUND32070. UP34,26known. REDDRAGON70,20DEAD32077corpseLEFT. HP160 XP1300031 SATIATED gON OOFF INVIS aWIELD. MAIN PICK bBLESSEDcarriedunencumberedwhenLEV,burdenedwhenOFF. BAGGED H EMPTYtested32011 (7uses lastD51dig49,18), J CREATE0:3,K CURSEDSLOW0:1,V MM0:2; mainFbellCANNOTBAGremains. BOH78now pickout. HOLYWATERZERO. LastmealSASQUATCH31980. LastOBS45:01:54~5min.
D51DOWN59,28↔D52UP45,22FOUND32000. NEWPICKSHORTCUT56,25 and25,22. FAST D51DOWN→UP:59,28SW58,29W57,29N57,25W53,25S53,27E55,27POLY(MRsafe)S55,29W51,29N51,27W47,27S47,29W37,29N37,27W33,27S33,29W29,29N29,27E31,27N31,25W29,25N29,23W25,23N25,21E27,21N27,18NE28,17E29,17N29,13W26,13. AutoTravelstopsbeforePOLYandB27,17; manualbypass! LEOCROTTA57,28DEAD32003;ETTINMUMMY57,25DEAD32006corpseLEFT. AllotherD51aliveasbefore.
LATEST D52T31996 hero43,21 HP161 XP1298949 SATIATED sasquatchmeal31980. VS22,23 PHYSICALLYVISITED31933. NEW FAST UP→VS:45,22N45,21W31,21N31,19W25,19S25,21W21,21S21,22SE22,23. PICKSHORTCUTS26,19 /36,21 /38,21 /42,21 /44,21 allOPEN. Avoid FIRE31,23. PICK b nowBLESSED consumedLASTHOLYWATER31939, noholywaterleft; currentlywieldedbutnextwaaysbstashthen662Rg<toD51. BOH74whilepickout;75whenrestashed. Sasquatch35,22DEAD31956ATE31980; MASTODON34,21DEAD31963corpseLEFT; MARILITH27,25DEAD31929weaponLEFT. Mindflayer20,15confirmed31925telepathy, lastwanderingwest15,15, aliveavoidmelee. Jabberwock21,13asleep. Otherformerpitmastodon41,18maySHAPESHIFTERnowx39,16 (telepathy31925noqpit). Nursewandering44,17last4warning. OBS45:01:54healthy245skips0congestion. Mainallunchangedexceptholywaterconsumed+pickblessed. gON OOFF INVIS AUTO OFF.
D52oldlongroutecontinuationfrom3,13:S3,17E5,17N5,15E7,15S7,17E9,17WEBbrieftrapped31874S9,19W5,19S5,21W3,21S3,23E5,23S5,27W3,27S3,29E9,29N9,25E11,25N11,23W9,23N9,21E15,21S15,23E17,23S17,25W13,25S13,27W11,27S11,29E15,29N15,27E17,27S17,29E19,29N19,27E23,27N23,25E27,25N27,23W22,23VS. No longerneedthisroute useSHORTCUTabove.
D52LATEST31864 hero3,13 HP161 XP1297759 unchanged. VS22,23stillnotreached. Routefrom31,19:S31,21E35,21N35,17W31,17N31,15W29,15S29,17W21,17N21,15W19,15N19,13W17,13S17,15W15,15S15,19W11,19N11,15W9,15N9,13W3,13NEXTSOUTH. JABBERWOCK21,13asleepaliveunengaged. UNEXPLORED35,21S35,22;33,17S33,18;19,13E20,13jabberwockbranch;9,13E10,13. Allmaze1tile. OBS44:45:16last~4min.
D52LATEST31823 hero31,19 HP161 XP1297759 NOHUNGER gON OOFF INVIS. NEXTS31,21EAST (FIRE31,23avoid). VS22,23notreachedyet. UP45,22known. MOUNTAINCENTAUR39,16dead31797corpseLEFT. MASTODON41,18stuckSPIKEDPITalive; secondMASTODONwandering22,19now5warning. JABBERWOCK21,13stationary. NURSEalivewandering45,25; mindless3follower37,24unknown; new1warning33,25unknown; stationary2warning27,25isDEMONinitial27,25unknownspecies.
D52UP→currentroute:45,22N45,20NE46,19E47,19N47,17W43,17N43,13W41,13S41,15W39,15S39,21E41,21S41,23W37,23S37,25E39,25S39,27W37,27S37,29W29,29N29,21W27,21N27,19E31,19. B45,19untouched bypass45,20↔46,19. UNEXPLORED41,21N41,20→POLY41,19→MASTODONpit41,18;43,13E44,13deadlikely;37,29E38,29deadlikely. Mainroutehugepotentialpickshortcutsfuture. OBS44:45:16healthy245skips0congestion.
D52UP45,22FOUND31783 (D51normalDOWNunknown). LATEST31783 hero45,21 HP161 XP1297612 NOHUNGER(nolongersatiated) gON OOFF INVIS. VS22,23goal NEXTN45,19.
D52landing→UProute:57,17N57,13W55,13S55,15W53,15N53,13W47,13S47,15E51,15S51,17E53,17S53,21E55,21S55,23W49,23S49,27E55,27S55,29W43,29N43,27W41,27N41,25E43,25N43,23E45,23N45,22UP. SQUEAK44,23LEVsafenoalert. Dead55,27N55,25W51,25; dead57,29. Unexplored55,23E56,23 /57,13E58,13 /55,21N55,20.
D52telepathy31772: TWO MASTODONS37,29(now41,22warning5) and26,29confirmed. NURSE45,27now47,22warning4 (initialhuman44,23). CENTAUR46,27wanderingnow48,17warning2. JABBERWOCK21,13stationary; DEMON27,25stationaryunknown; SPIDERS35,23/71,17; COCKATRICE62,13unknownkind; OGRE62,27unknownkind. Mindless3followingfrom59,17nowmaybe52,27couldgolem notidentified. Noother52killsbesidesMINOT+CLAYGOLEM. OBS44:36:04last~5mindue.
D52T31726 hero57,13 HP161 XP1297612 AC-19 Dx18 gON OOFF INVISIBLE SATIATED. CLAYGOLEM58,13dead31726 rocksLEFT. New3warning59,17mindlesslikelygolem;4warning50,19maybeDEMON initial27,25. UPunknown VS22,23known.
D52ALLTRAPtypesconfirmed: TELEPORT28,13; FALLINGROCK67,15; ROLLINGBOULDER67,16/63,20; SPIKEDPIT41,18/65,29; POLY41,19; FIRE31,23; SQUEAK44,23; STATUE61,25; WEBS9,17/77,19; VIBSQUARE22,23. RouteLanding57,17N57,13 thenWESTnext. East58,13alsopassageunexplored.
LATEST D52T31721 hero57,17 HP161 XL18/1297289 AC-19 DxRESTORED18byax31713 gON OOFF INVISIBLE SATIATED31590. VIBRATINGSQUARE22,23 CONFIRMEDfarlook31721 glyph~! UPUNKNOWN; landing57,17 viaD51TRAPDOOR49,16T31708. GoalmapVS+UP thenreturnD48portal39,21→WizardBOOKstillnotobtained.
ORB D NOW(0:0) first52apply31711FAILEDblind; ax31712fail axax31713restoredDx18andvision. Second52apply31713^SUCCESS lastcharge. Fulltraps: VS22,23; ^28,13/67,15/67,16/41,18/41,19/63,20/31,23/44,23/61,25/65,29; webs9,17/77,19. Farlooktypespending. Successfulorbhelpless10maxafterexit: Escapealone+screen+11dots resolvedsafe;T31721nowcommandsnormal. AUTO OFFunchanged.
MAINmDEATH NOW(1:2) FIFTHherochargeD52S57,17killedMINOT57,18T31710. Reflectedreboundnoharm corpseLEFT. MAINHdigNOW7HEROUSES N49,19D51opens49,18 shortcuttoTRAPDOOR49,16T31706. Otherinventorysame BOH76 includesMAKEINVISwandj1hero+selfknown; PERMINVIS gained31772? correction31672.
D52initialtelepathy31709: MINOT57,18dead; JABBERWOCK21,13; CENTAUR44,17; SPIDERS9,18/77,18; QUADRUPED29,19+16,27; HUMAN44,23unknown; DEMON27,25unknown; COCKATRICE72,23unknownkind; OGRE63,29; mindless4initial60,17 now61,15 and49,17 (new4couldDEMON); 3warning61,17 mindlessprobablygolem. NarrowLITmaze here visiblewalls andfloor· unlike51darkno wallsfloor▒.
D51finalroute61,25E63,25S63,27E65,27N65,23W63,23N63,19E65,19N65,17W63,17N63,15E65,15N65,13W59,13S59,17W55,17S55,19W49,19N49,16TRAPDOOR viaDIG49,18. ELF-LORD59,13dead31696 armorLEFTunsearched. UP26,13stillonlystairsfound normalDOWNUNKNOWN. Trapdoorfell31708→52landing57,17. LastOBS44:36:04healthy.

OLDER:
D51LATEST31672 hero61,23 HP161 XP1296348 SATIATED gOFFwillON. NEWINVISIBILITY fromselfzapj31672 (wandmakeinvisible fromELF-LORD61,23killed31668; picked31671,1HEROUSE+1monsterknown31660). BAGGINGjnext BOH76. Otherinventoryunchanged. FORESTCENTAUR53,26dead31655 corpseLEFT. ELF-LORDsecondALIVE65,25flednotattacked. Other3warning67,25unID,2warning60,27unID+66,21unID.
D51routecontinuation35,27E37,27S37,29E47,29N47,27E51,27S51,29E55,29N55,27(POLYMRSAFE)W53,27N53,25E55,25N55,23E59,23N59,19E61,19S61,23nextS61,25. DEAD39,27. UNEXPLORED43,29N43,28 and49,29WEST49,28? at49,29W48,29blanklikelydeadbutnotchecked. ARMOR55,28LEFT. Firstcentaur37,29chasedthen53,26dead; passedPOLY55,27withoutchange. OBS44:36:04healthy245skips0congestion.
D51LATEST31632 hero35,27 HP161 XP1296085 gON OOFF SATIATEDlastmeal31590. PYROLISK20,27dead31598noinventoryharm; GLASSGOLEM26,23dead31608 glassLEFT. Minotlast36,19alive. New3warning30,19unknownspecies. Routefrom17,27:N17,25E19,25S19,27E23,27S23,29E25,29N25,23E29,23S29,25E31,25S31,27W29,27S29,29E33,29N33,27E35,27EASTnext. Dead35,25/35,29. 25,29E26,29UNEXPLORED. Allinventoryunchanged.
D51LATEST31590 hero16,27 HP161 XP1295346 SATIATED ogrekingmealfinished31590. gOFFwillputONnext. SALAMANDER15,20dead31544corpseLEFT; OGREKING16,27dead31571ATE31590. Nocharges/inventorychanges. Routefrom19,13: S19,17W17,17N17,15W11,15S11,21E13,21N13,17E15,17S15,21E17,21N17,19E21,19N21,17E23,17S23,25W21,25N21,21W19,21S19,23W15,23S15,27E17,27NORTHnext. OBS44:30:06healthy245skips0congestion.
D51UP26,13FOUND31501 connectsD50normalDOWNunknown. Branchfrom23,13S23,15E25,15S25,21E27,21N27,18NE28,17E29,17N29,13W26,13UP. B27,19pushedto27,17T31495 bypass27,18↔28,17. UPbranch25,13dead/27,13S27,15dead. 23,15W21,15dead. NEXT19,13SOUTH. Landing→northernroutecontinued3,15E5,15S5,19E7,19S7,21E9,21N9,15W7,15N7,13E23,13. 5,17EASTunexplored shortcutmaybe. D51MINOT29,20confirmed; mindless5warning27,23likelyIRONGOLEM; OGREKING25,23; SALAMANDER21,23. Last31519 HP161 noinventorychanges.
D51exploration31458: southwestmainroute landing16,29W13,29N13,27W9,27S9,29W3,29N3,23E5,23N5,21W3,21N3,15. 3,15N3,13E5,13DEAD;NEXT3,15EAST. Nurse18,29dead31404; longworm12,25dead31413 corpsesLEFTnotate. Deadbranch13,27N13,25W9,25N9,23(SLEEP)E13,23dead; from9,23W7,23S7,27W5,27N5,25dead. 11,29WESTstillunexplored. Nochanges HP161 XP1294845.
LATEST D51 T31401 hero19,29 HP161/161 XL18/1294204 AC-19 gON OOFF AUTO OFF. HostileNURSE18,29 blockingwest. East21,29DEAD;19,29Nwall. Needwestotherbranch. D51UP/DOWNUNKNOWN; landed16,29 viaD50TRAPDOOR12,16T31385. D51TRAPDOOR49,16 targetdeeper; NO VS all8trapsfarlooked.
ORB D NOW(0:2) successfulD51apply31388^; trapdetect: ROLLINGBOULDER33,14; SQUEAK3,15; TRAPDOOR49,16; SLEEP25,19/9,23; FIRE69,23; BEAR51,25; POLY55,27. Artifactcannotexplode;50%Int10failureconsumescharge. SuccessfulmapexitCAUTION: nomul1..10helpless, EXITESCALONE thenSCREEN beforeinput! @accidenttoggledautoON but correctedOFF31397.
D50 UP34,26 toTRAPDOOR12,16route: N34,25W22,25N22,22W18,22S18,26W12,26N12,19W8,19NW7,18N7,16E12,16. AVOID FIRE30,26 viaROW25. D50normalDOWNUNKNOWN. BALUCH29,25dead31351;SHOCKSPHEREexploded31356noharm. BLACKDRAGON10,16woundedFIVEhits31380..82 FLED31383 ALIVE. FellD51T31385. OtherD50initialmonstersaliveexcept2spiders+minot+baluch+sphere.
D51initialtelepathy31386: NURSE12,29now18,29; MINOT29,21CONFIRMED; LONGWORM7,27; OGRE29,29; LIZARD30,29; COCKATRICE44,23; QUADRUPEDS64,23/67,25; MIMIC74,19; DRAGON77,27. OthersunID. Nofood/inventorychangesexceptOrb0:2 sinceD50below. MAINmdeath1:3, BOH75. Lastmeal31240. OBS44:23:47healthy245skips0congestion. PublicnoteD51.

OLDER:
LATEST D50 T31349 hero30,25 HP155/161 XL18/1293712 AC-19 Dx17 gON OOFF. NEXTq29,25farlook pending. UP34,26↔D49DOWN71,17. DOWNUNKNOWN. NO VIBRATING50 fulltrapdetect31338 confirmsneeddeeper.
ORB D NOW(0:3): firstapply31336failedcomprehend, secondapply31338^successfulFULLTRAPDETECT. Traps: FIRE30,26/61,24/55,14; BEAR6,14/27,14; MAGIC19,13; TRAPDOOR12,16; LEVELTELE72,26; WEBS23,20/31,20.
MAINmDEATH NOW(1:3) fourthHEROUSE31342 N36,25killedMINOT36,24 +probablyspider36,23. rORCUSDEATH EMPTYtested31341 then8accidentmeleeminot; BAGGED31343 BOH75. NOsecondherochargeduse ronly1successfulD47. Allothermainunchanged eLIGHTNING0uses,pSTRIKE5,Hdig6,Zdig7.
D50GIANTSPIDER31,25dead31347 corpseLEFT;MINOT36,24corpseLEFT. q29,25approaching. Up34,26W30,26FIREavoidROW25. DarkWIDE2tilecorridor, explorebothsides.
D50initialtelepathy31335:MINOT34,21nowDEAD;DRAGONS13,16/70,19;DEMONS71,13/70,14;NAGA57,19;SPIDERS32,20/24,21bothdeadlikely;COCKATRICES45,21/40,25;CENTAUR43,25;QUADRUPED17,26now29,25. ELF?human2warning36,16new. LastfoodETTIN31240.
PublicnoteLevel50seekingdeeper. OBS44:10:12healthy(lastatD49down).

OLDER:
LATEST D49 T31332 hero73,17 DOWN71,17FOUND;next44Rg>to50. HP161/161 XL18/1292842 AC-19 Dx17 gON OOFF. LastmealETTIN31240.
D49 FINALDOWNROUTEcontinuation59,21E65,21S65,23W63,23S63,25W59,25N59,23W57,23S57,26SW56,27SW55,28S55,29E62,29NE63,28N63,27E65,27N65,25E69,25N69,21E71,21N71,17DOWN.
NEWMAIN e LIGHTNINGfromPITFIEND57,25picked31311 UNKNOWNBUC0herouses fiendONEuse31306. FiendDEAD31309, flashblindcuredax31310. Nootherinventorychanges. BOH74.
B57,27/B55,27 untouched bypass57,26↔56,27↔55,28;B63,29untouched bypass62,29↔63,28. Dead61,23east. UNEXPLORED55,29WEST;63,27WEST;73,17SOUTH;41,15WEST;19,13SOUTH.
ShapeshiftersMULTIPLEseen31308 whileblind:OLOG→DISENCHANTER43,17;XAN→XORN43,20;LEOCROTTA→XORN31309. LikelyDOPPELGANGERSmany. Kraken41,18stillinFAKEWIZ2leftundisturbed. SeveralGIANTS3warningsnear63..69,19;JABBERWOCK67,13stationary5;ELF-LORDteleportedawayalive35,15seenblind. QUANTUM51,19. DEMON49,27 unknown;DEMON27,29unknown newtelepathy31308.
OBS44:10:12 healthy245skips0congestion.

OLDER:
LATEST D49 T31288 hero59,21 HP158/161 XL18/1292264 AC-19 gON OOFF. DxNOW17exercise31276. NEXTeast60,21. DOWNUNKNOWN. LastmealETTIN31240.
pSTRIKING FIFTHHEROUSE31262 brokeB52,13(original47,13pushed) hitWRAITH; Tfreshstill0uses. B35,13pushed→41,13T31251 bypass40,13↔41,14. B31,15untouched bypass31,14↔30,15. B27,19untouched bypass27,18↔28,19.
D49routecontinuation:27,15W25,15S25,17E27,17S27,18SE28,19E29,19N29,17E31,17S31,19E33,19N33,13E40,13SE41,14S41,15E43,15N43,13E55,13S55,17E57,17N57,15E61,15S61,17W59,17S59,21.
Deadbranches23,15west;31,13S31,14SW30,15W29,15N29,13DEAD. UNEXPLORED41,15WEST;19,13SOUTH. Entireeasternareaunexploredexceptcurrentroute.
DEADPITFIEND27,17T31203;VAMPIRE LORD32,13dead31218(afterwolfshape);ETTIN31,13dead31221ATE31240;WRAITH54,13dead31264NOcorpse;HELLPUPS56,17dead31274/60,17dead31284.
INVISELF-LORD55,14T31268 wounded2hits TELEPORTEDAWAYalive. SeveralGIANTS3warningsnear57..65,13..17;JABBERWOCK67,13stationary5;DEMON57,25stationary4unknown;severalother2warningselves/quantum. WesternSHAPESHIFTER5near25,20, ZRUTY39,21 andBAT39,20alive.
BOH74 unchanged mainlockingbaggedearlier. Hdig6 Zdig7 rdeath1 mdeath1:4 unchanged. OBS44:03:49healthy245skips0congestion.

OLDER:
LATEST D49 T31195 hero27,15 HP161/161 XL18/1290201 AC-19 gON OOFF. NEXTWEST26,15unexplored. DOWNUNKNOWN. PITFIEND21,13dead31188-90. LONGWORM7,22dead31162 corpseLEFT.
NEWLOCKINGwand11,21 pickedMAINd31147 BAGGED31148 BOH74items (unknownBUC fresh0uses). Nootherinventorychange. Lastfood30908.
D49WESTKNOWNROUTEfromUP:25,29W23,29N23,28NW22,27W21,27N21,25W13,25S13,29W9,29N9,27E11,27N11,25W9,25N9,23W7,23N7,21E9,21N9,19W7,19N7,15E11,15S11,17E13,17N13,15E15,15N15,13E26,13SE27,14S27,15.
B23,27 untouched bypass23,28↔22,27;B27,13 untouched bypass26,13↔27,14. B3,19deadbranch untouched. ROLLINGBOULDERtrap3,29noBreleased31111.
D49WESTDEADbranches:UPW19,29N19,27W17,27S17,29W15,29N15,27DEAD.13,29W7,29N7,25W5,25S5,27W3,27N3,21E5,21N5,17W3,17N3,15E5,15N5,13E13,13DEAD(W3,13DEAD).3,27S3,29E5,29DEAD;5,21S5,23DEAD;3,17S3,18B3,19DEAD.9,19N9,17DEAD;15,15E17,15DEADgoldLEFT.
UNEXPLOREDjunction19,13S19,14 (passed), current27,15WEST. Mostwesternmaze mapped. Warningchanging5/2/3/4westerninsideoriginalUPbranch probablySHAPESHIFTER cannotreachunlesslongroute.
OBS43:58:00 healthy245skips0congestion.

OLDER:
LATEST D49 T31031 hero15,17 HP161/161 XL18/1289312 AC-19 gUNCLEVON OOFF. NEXTsouth15,18unexplored. EAST19,17DEAD.
D49UP25,29↔D48DOWN77,24;DOWNUNKNOWN. MainrouteUP25,29E27,29N27,27W25,27N25,25W23,25N23,23W21,23N21,19W17,19N17,17W15,17.
D49southernbranchdead:23,23E26,23SE27,24S27,25E29,25N29,23E31,23S31,26SW30,27W29,27S29,29E35,29DEAD;33,29N33,27DEAD.21,21E23,21DEAD.
D49B27,23 untouched; B31,25pushed→31,27T30994; bypass31,26↔30,27. XORN36,29dead31003. Gold31,23/31,25/27,29LEFT.
D49telepathy30978:DEMONS21,13/27,17/57,25/49,27 unknown;ETTIN29,18confirmed now24,15warning3;DOG26,17;JABBERWOCK67,13;GIANTS65,15/65,17/66,17/67,17;DOGS55,16/56,17+HUMAN55,17;WRAITH57,16;QUANTUM46,17;ZRUTY38,21;BAT39,22;KRAKEN40,24(fakewiz2SKIPinside).
OBS43:53:27 healthy245skips0congestion. LastFOODstormgiant30908. Allinventoryunchanged BOH73 mainHdig6herouses.

OLDER:
LATEST D48T30975 hero77,21 DOWN77,24FOUND;next222Rg>to49. HP161/161 XL18/1289087 gON OOFF. PORTAL39,21known.
D48DOWNROUTEcontinuationfrom63,23: W61,23 S61,25 E63,25 S63,27 E67,27 N67,25 E74,25 SE75,26 S75,29 E77,29 N77,24DOWN.
B73,25pushedto75,25T30967; bypass74,25↔75,26. ARMOR75,27LEFTunID. No newtraps.
UnexploredD48branches45,22S;75,29WEST;77,24Npast77,21 etc. Downrouteallknownnoadditionaldig.

OLDER:
LATEST D48 T30953 hero63,23 HP161/161 XL18/1289087 AC-19 gUNCLEVON OOFF. DOWNUNKNOWN. PORTAL39,21undisturbed.
HdigSIXherouses: latestD48E40,21opens41,21T30910 EASTEXITtower useful! PORTAL→eastmaze:39,21E43,21(overmoat42,21) S43,22 E45,22 thenN/Sjunction. Don'tactuallystepPORTALyet.
STORMGIANT39,23dead30871 corpsefinished30908 afterinterruptions,Ststill18/21. FOODlast30908;ONECmain.
OWLBEAR40,21dead30867;HELLPUPS totalFOURdead(39,25 30863;39,24 30887;39,22 30903;39,22 30906). GREYELF39,23dead30895. ZRUTYwounded2hits30876fledlast42,25alive. MARILITH38,25identified30908alive pursuing. New4warningat39,27unknown. Purpleworm/dragon alive west ofshortcut32,19 and mayfollow.
ELVENKING60,17dead30943 droppedPICKAXE pickedMAINb30944 BAGGED30945 BOH73items. PICKUNKNOWNBUC DO NOTWIELDwithoutcursecheck(orholywaterready). Restlootcorpse+elvenbroadswordLEFT. Another3warningwanders61..65,13..15 unknown,plus3@71,14.
PORTAL→CURRENTroute:39,21E43,21S43,22E45,22N45,21E47,21N47,19W45,19N45,17E49,17N49,13E51,13S51,17E53,17N53,13E55,13S55,17E57,17N57,15E59,15S59,17E63,17S63,19W61,19S61,21E63,21S63,23CURRENT.
UNEXPLOREDjunction45,22S45,23 (northernpathabovealreadydone), at63,23WEST62,23(currentnextW8sent). RING55,17LEFTunknown. NOtrapsoutsideTOWER48sofar.
OBS43:42:09healthy245skips0congestion. Publicnoteportal48foundseekingvibrating.

OLDER:
LATEST D48 T30866 hero39,22 HP161/161 XL18/1287380 AC-19 gON OOFF. FAKEWIZARDPORTAL39,21 FOUND30866 underARMOR. Don'tstepuntilready. BOOKstillWIZ40asleep. DOWN48UNKNOWN.
D48 UP4,17↔D47DOWN61,16. D48realFAKEWIZ1withPORTAL, no needD46forportal! StillneedVibratingSquarebelow.
D48TOWERoffset35,17,moat36..42 y18..24, center39,21PORTAL, SQUEAK38,21/39,20/40,21/39,22. DugSOUTH39,23 H5th30858. WallsnoDoors. Levnecessarywater;krakenDEAD40,24T30858.
MAINgNOWUNCLEV blessingremovedNalfcurse30816. Allarmor/MR/freeaction/reflection/Orb/BOHremainunchanged confirmedinventory30819. OtherUNKNOWNwandspossiblycurseundetectable. HdigFIVEHEROUSES now, fourthD48E31,19 opens32,19T30778; fifthN39,24 opens39,23T30858.
D48UP→PORTALknownsafeLONG route:4,17E5,17S5,21W3,21S3,23E11,23N11,21E13,21S13,25E17,25S17,29E29,29N29,25W26,25NW25,24N25,23E29,23N29,21E31,21N31,19E33,19(DIG32,19)S33,23W31,23S31,29E33,29N33,27E35,27N35,24SE36,25E39,25N39,22(DIG39,23). Lastsegment39,24LEVONoverwater. B25,25 pushedfrom27,25 bypass26,25↔25,24.
D48NORTHDEADBRANCH33,19N33,17W31,17N31,15E33,15N33,13E35,13S35,15E37,15N37,13E39,13S39,15E43,15N43,13E45,13S45,15E47,15N47,13DEAD.
Remainingfrontiers:31,13WEST (row13x31..35 leftunexplored),41,13WESTdeadprobably;UP3,16NORTH;15,19SOUTH;17,29WEST; D48EASTENTIRELYUNEXPLORED needDOWN. Centraloutereast43,22→maze ismainexit per yendor.des.
D48DEAD:HEZROU5,19 30690, LEO4,17 30691, CENTAUR5,19 30693, RUSTMON38,13 30792, LURKER45,13 30800, NALF32,19 30817(after2hits30736teleported thenreturnedcurse), QUANTUM33,27 30839, INVISGREYELF35,19 30847, TROLL35,23 30851(revivable), KRAKEN40,24 30858, YETI39,23 30861, HELLPUP39,25 30863.
D48ALIVEcurrentOWLBEAR40,21woundedONEHIT30866(nextF9F9F9sent), STORMGIANT39,24elvenshortsword(throwsBOULDERfilledmoat36,22+39,24 maybe39,24stillwater), trollreviving35,23, HELLHOUNDPUPSat43,24/42,25plusothers, ZRUTYwest35,19maybe, PURPLEWORMinitial11,16+DRAGON16,15nowmovingwest warning5towardshortcut33,19. OGRE/RUST?3@32,15new. GENOLmeansroomlichreplaced? ROOMOWL/yeti spawned random.
FOODlastTROLL30653; ONECrationmain. EATnothing48yet. rDEATH1herouse,m1:4,allotherchargesunchanged. OBS43:29:44healthy245skips0congestion.

OLDER:
LATEST D47 T30683 hero60,16 HP161/161 XL18/1283544 AC-19 gON OOFF. NEXT6Rg> DOWN61,16.
D47 DOWN61,16 FOUND30683. Route fromUP24,16 to49,26 seeolder; then E52,26 N52,25 NW51,24 N51,19 E60,19 N60,16 E61,16DOWN.
BOULDERS52,24 and52,21 bypassLEFTcolumn51. NEW FIRE51,17 avoidviaROW16. Ring60,17LEFT unknown.
D47 GIANTMIMIC37,18dead30598, GREYELVES46,18/51,14/51,13dead30617..30626 (3dead;remainingonealive), ROCKTROLL49,20dead30638 atefinished30653, OCHREJELLY51,23dead30671.
FreshFOODtroll30653, stillONECmain. No wand charges since30441. Dx18 restored30561 afterxan18,15injury30520(killed30522).
WESTmaze x3..19 exploreddeadends, LANDMINE3,13/DART3,14/B4,18/B9,26. SQUEAK16,14.
UNKNOWN5warningnear55,16 NOTvisibletelepathy (mindless, maybeIRON GOLEM); NOshotsusedonit.
OBS43:23:02healthy245skips0congestion.

OLDER:
LATEST D47 T30479 hero23,13 HP161/161 XL18/1282268 AC-19 gON OOFF noHUNGER.
D47 UP24,16 FOUND30479↔D46DOWNUNKNOWN (D46notvisited);D47DOWNUNKNOWN. NewMAIN T STRIKINGfresh0herousesfrom26,16picked30477.
E NOWONE UNC C-RATION main afterate30475. MAIN LextrahealingunknownBUC. BOH72items.
r ORCUSDEATH FIRSTHEROUSE30441 killedMINOTAUR40,13;remainingchargesunknown (notempty). mUNCHANGED1:4.
GARGOYLE41,13dead30444; NURSE28,26dead30413;corpseleftDONOTEATnursehuman.
D47FIRES20,19 /40,19. Avoid40,19via40,18SE41,19 or39,19SE40,20.
B21,20bypass21,21NW20,20NE21,19;B22,13 justfound;B48,16 can'tpushWESTwall.
IMPORTANT DARKWIDECORRIDORS2tileswide: sweepBOTHedges, traversingrow26onlymissednorthbranch39,24 offROW25! Don'tdeclarewholewingdeadwithoutbothboundarieschecked.
CURRENTUP→LANDINGreverseknownroute:24,16E25,16N25,13E27? WALL26,13: use25,16E27,16N27,13E34,13S34,16W30,16S30,22E36,22N36,13E43,13S43,19W41,19NW40,18W39,18S39,25E46,25N46,22W45,22N45,13E52,13S52,16W49,16S49,26E54,26(DIG53,26)N54,22E57,22S57,25E66,25N66,24LANDING.
MorepreciseUP24,16→27,16 directROW16allopen. Goodpastnewwand26,16.
D47SOUTHROW26continuous24..46. DEADWESTloop24,26N24,22W21,22N21,21NW20,20W18,20N18,19dead; ROW19x18..28 FIRE20,19;28,19S28,23dead.
CENTRAL39,25N39,16DEADTOP, but40,18SE41,19E43,19N43,13W36,13S36,22W30,22N30,16E34,16N34,13W27,13S27,16W24,16UP.
OptionalUNKNOWNAMULET36,20LEFT. INITIALMIMIC37,18stationarywarning3 NOWv37,18 (coulddisguisedmimic/crystal? don'tassumevortex). TROLLlast52,20alive.
Greyelves4alivefollowing(east) allnurse/minot/gargoylenowdead. OBS43:11:32healthy245skips0congestion.
StillNOFAKEWIZARDTOWERSlocated;D46SKIPPEDlikelyoneof46/48/49 etc. NeedsearchbeforeWizard.

OLDER:
LATEST D47 T30359 hero46,13 HP161/161 XL18/1281100 AC-19 gON OOFF noHUNGER. UP/DOWNbothUNKNOWN.
D45TRAPDOOR71,17fellT30245SHAFTtoD47landing66,24;D46SKIPPED/unvisited.
D47WRAITH61,25corpseate30258 gainedXL18+7HP. AGATERINGsamefloorpickedPbagged30262 BOH72items.
MAIN L UNKNOWNBUC EXTRAHEALING fromD45hezrou60,13; oldL OAK=SPEEDMONSTER1engraveuseBOH.
D47killLYNX66,16T30273;XAN76,20T30297;MASTODON50,25T30339;ETTINZOMBIE50,25T30344. Mastodon+ettincorpsesleftnotate.
ROCKTROLLALIVE last52,19T30359 withRANSEUR. GREYELVES4alivewounded2,following;lastone48,22. UnID4@43,13 approachingCURRENTwest (Hinitial29,14 maybeettin/minot).
MainmDEATH1:4 (lastD45minot30069),HfreshDIGTHREEuses lastD47W54,26T30333opens53,26;priorD45opens42,21+55,14. pSTRIKE4uses, otherchargesunchanged.
D47DARKWIDECORRIDORMAZE. Landing66,24N66,22E67,22dead;S66,25W60,25S60,26W57,26N57,22W54,22S54,26W49,26(DIG53,26)N49,16E52,16N52,13W46,13CURRENT.
EASTLOOPnoSTAIRS yet:60,25N60,22E64,22N64,20E70,20S70,26E76,26N76,13W72,13DEAD(72,14alsodead).
Otherdeadbranches:64,20N64,16W63,16dead/E67,16dead;70,20N70,19dead;67,22dead;B48,16can'tpushWwall.
EasternjunctionUNEXPLORED:70,22E72,22thenNEdark (elvescomehere),76,20W74,20thenNWdark,52,13E?? (onlywentwest),55,22E58thenSloopdone.
BouldersD47 66,26/69,26/48,16 untouched. NOtrapsyet exceptSQUEAKheardbutlocationunknown30258.
OBS43:03:50healthy245skips0congestion.

OLDER:
LATEST D45 T30243 hero71,15 HP154/154 XL17/720142 AC-19 gON OOFF noHUNGER. NEXT22Rg intentionallyTRAPDOOR71,17descend.
D45 DOWNstillUNKNOWN. TRAPDOOR71,17; ARROW73,19 (arrowobjectontrap). ALLNE x67..77,y13..23 DEADENDnetworkapartfromtrapdoor.
NEWroutefrom55,23N55,17W53,17N53,15E55,15N55,13(DIG55,14Hsecond30171)E57,13S57,15E59,15N59,13E67,13S67,17E69,17N69,13E77,13S77,17W75,17N75,15W73,15S73,17W71,17TRAPDOOR.
NEextra:71,17N71,15DEAD;S71,21E75,21N75,19W73,19DEAD/ E77,19S77,21DEAD;71,21S71,23W69,23DEAD.
H freshDIG TWOherouses(42,21;55,14). pSTRIKE FOURherouses:clearedB60,13 T30181.
3HEZROUs dead60,13(30184),61,13(30187),67,14(30196). L MAINNOWUNKNOWNBUC EXTRAHEALINGpotion from60,13 picked30189.
NWunknownotherdemonsstillalive;quantummechanic(warning2)73,16followinglast30243. Doesn'tthreatenMRbutteleporthitpossible.
Deadbranches53,17W49,17dead,53,15E55,15wasdeadbeforeDIG;55,27WESTunexplored;53,13WESTunexplored;63,13S63,14unexplored.
OBS42:54:43healthy245skips0congestion.

OLDER:
LATEST D45 T30158 hero55,23 HP154/154 XL17/719155 AC-19 gON OOFF noHUNGER.
D45 UP3,16 DOWNUNKNOWN. MINOTAUR22,13deadmDEATH30069 thirdherouseNOWm1:4; corpseLEFT.
BONEDEVIL21,15dead30075 gemleft. VAMPIRE44,29dead30118. QUANTUMmechanic17,14woundedteleportedaliveunknown2east62,17last.
Shapeshifter3,19(Aleax→zruty→Elvenking→5warning→human10,15)ALIVEfollowingwestcouldstrong; don'tassumepeaceful.
H freshUNCdig FIRSTuse30102 E41,21→42,21 shortcut. Otherwandchargesunchangedsince44.
D45UP→CURRENT route3,16N3,13E7,13S7,16 (B7,15PUSHEDto7,17) SE8,17E9,17N9,15E11,15N11,13E23,13S23,15W19,15S19,17E25,17S25,21
E39,21S39,25E41,25N41,21E43,21(DIG42,21)S43,23E45,23S45,25W43,25S43,27W39,27S39,29E45,29N45,27E49,27S49,29E55,29N55,23CURRENT.
D45DEADBRANCH row29E55→63,29N63,27W61,27DEAD;63,27E65,27S65,29E69,29N69,27W67,27DEAD. NOstairsinSEloop.
UNEXPLOREDjunctions3,17E/south;17,13S17,14;25,21WEST;31,21N;33,21S;43,21N;39,29WEST;49,27N;49,29WEST47,29;55,27WEST;55,23Ncurrent.
NoD45trapsidentifiedyet. B7,17canbypassdiagonal8,17↔7,16. D45northwestloop9,13deadgold.
BoneDEVILS27,17+27,18 and47,23+48,23ALIVE;otherDEMON53,19warning2unknown.
OBS42:47:47 healthy245skips0congestion.

OLDER:
LATEST D45 T30042 heroUP3,16 HP154/154 XL17/717670 AC-19 gON OONaftertelepath nextRO.
D45telepath MINOTAUR19,20;ZRUTY3,19 (AleaxturnedintoZruty: chameleonORPOLYtrap);Q19,16;DEMONS27,17+28,17+27,18 /53,19 /47,23+48,23;BAT63,28.
D44 UP25,18↔D43DOWN66,28;DOWN14,24↔D45UP3,16. DARKWIDECORRIDORMAZE.
FAST D44UP→DOWN25,18W23,18S23,24W14,24. FIRE24,20 avoidx23;FIRE35,23avoidROW24.
D44UPeastloop25,18E36,18S36,25W14,25; B36,19 bypass35,19;B32,19. UNKNOWNotherleveloutsideboxx14..36 y18..25.
D44killedGIANTZOMBIE24,18 (followedstairs),GLASSPIERCER23,23. SCORPION35,22alive;wandering4(last14,21)unknown.
D44telepathinitial:TRAPPER4,13 YETI67,18 MIMIC41,19 DEMON53,19. Don'tknowfakeWizardtowerlocationsyet.
L OAKwandtestedengraving30010="bugs speed up": SPEEDMONSTER ONEherouse, NOWBOH71items.
Excalre-wielded30009 aftermistypednewlineaccidentxswap; mainaISWIELDED.
D43VAMPIRE39,20dead29980;bat72,28alive. D43GIANTZ67,29followed44dead30001.

OLDER:
LATEST T29945 D43 hero3,26 HP144/154 XL17/716870 AC-19 gOFF OOFF noHUNGER.
ORCUS DEAD29915 at4,27. Loot rUNKNOWNDEATHwand5+monsteruses; AUNKNOWNMAGICMISSILEwand MAIN. cursedaklysLEFT4,27.
MINOTAUR3,26dead29926 after vSLEEPthirdherouse +6Excalhits; SLEEPWAKESonmelee soNOTlongfreeze. ShockingSPHEREsamepositionkillednext2hits.
AteMINOTAURfinished29945. H MAINNOWFRESHUNC DIGfromHome3 retrievedBOH29921 ZEROherouses; OLDHempty+eCURSEDEMPTY nowBOH. BOH70items.
ONEremainingunusedDIGunknownHome6inBOH amongseveralemptyunIDcopies. NewrDEATHchargesunknown. Originalm1:5untouched.

OLDER:
LATEST D43 ORCUS-TOWN T29914 hero5,27 ONUPSTAIRS HP131/154 XL17/714746 AC-19 gON OOFF.
ORCUS ALIVE INVISIBLE4,27 adjacentWEST, nextF4. Ownupstairs preventsusualretreat. Minotaur7,22warning5 approaching, unknown2@7,25.
Orcus deathwand5+chargesusedREFLECTEDsafe; melee/spellheadachecanhurt (154→131onecycle), keepHPwatch.
Orcus curse29856: mDEATH nowUNC1:5, YPOLY nowUNC1:6, eDIG nowCURSED0:0. Armor/rings/Orb/BOHunchanged.
Q GDSM actuallyBLESSED+1 verifiedinventory. BOH69items. EfoodMAIN2UNC C-rations lastate29769.
H DIG EMPTYtested29901 after6herouses; eDIG EMPTYlast29903. Z DIG7herousespotentialfewleft.
TWOunusedDIGwandsBOH retrieveafterOrcus. pSTRIKE3herouses. L UNKNOWNOAKwandVladtop28,16MAINunused.
D43 UP5,27↔D42DOWN12,15; DOWN66,28. ORCUS-townNOtele shortsighted. MOLOCHaltar57,20 avoid.
D43 digshortcuts32,23(H5),64,28(H6),12,29(eLAST). FIRSTtwoadded29769/29837,last29903.
FASTUP→DOWN:5,27E7,27S7,29E25,29N25,27W23,27N23,21E25,21S25,25E27,25N27,23E29,23S29,25E31,25N31,23E33,23N33,20E53,20S53,23E61,23S61,28E66,28.
TRAPS SLEEP33,16 FIRE46,19 ANTIMAGIC51,19. UseROW20avoidsfire/anti. No13,27digshortcutmade.
D43killssince29740:ogreking33,14,titanothere33,18,vampLord42,18,titanothere46,19,ettinzombie46,20,shade45,19,vampLord47,20,humanZ45,20,cock53,23,ettinZ61,27,flamingsphere65,28,humanZ65,28,shade63,28,humanZ63,27+63,29,vamp61,26,giantZ57,22.
BLESSEDEXCALhit/killedSHADES 6–8hitsworks. WRAITHSmorgue55..58,25..29alive couldlureoutsideforcorpses.
NWshop45..48,13..17 manyMIMICS;SEshop65..70,22..25 manyMIMICS;bothlootUNSEARCHED.
Wanderingbat40,20/shade42,20/giant+ettinZ40,22+40,25behindus. BONEDEVILS3western17,15..17alive.
OBS42:40:57 healthy245skips0congestion. PublicnoteOrcus-townreflection/MRready.

OLDER:
LATEST D43 T29740 hero23,21 HP154/154 XL17/710363 AC-19 gON OOFF noHUNGER.
D43 UP5,27↔D42DOWN12,15; DOWNUNKNOWN. MAINiCANDEL7unlit, Fbell0:3, noBOOKyetWizarduntouched.
D42SHORTCUTMADE N13,23→13,22HdigFOURTHuse29683. VLAD11,23E13,23N13,17W11,17N11,15E12,15DOWN.
D43 routeUP5,27E7,27S7,29E11,29N11,27E13,27N13,23E15,23N15,21E17,21S17,23
E19,23S19,25E21,25S21,27W17,27N17,25W15,25S15,29E25,29N25,27W23,27N23,21CURRENT.
B17,29pushedto20,29 thenblockedsecondB21,29. BOTHBROKEN pSTRIKETHIRDherouse29723 (previous2D42).
Cockatrice21,29dead29725corpseLEFT. PITVIPER23,25dead29735corpseLEFT. Lowboots17,29/gems17,25gold25,27/weapon23,27LEFT.
D43 firsttelepath: MINOT12,17;3BONEDEVILS17,15/16,17/17,17; OGRE35,17; quadrupeds37,23/62,28;
MIMICS9at45..48,y13..16 and7at66..70,y22..25;WRAITHS55,25/55,26/56,26/55,29;COCKATRICE52,25;
DEMON66,28unknown; BATSseveral43,16/48,17/45,19/68,17/67,29/68,29 others. Noneengagedexceptpitviper/cockatriceSW.
OTHERD43west x3..13,y13..25 unknown; knownjunction13,25WESTunexplored/15,21WESTunexplored/7,29WESTunexplored.
VladBOTTOM trollREVIVEDkilledagain29,20T29622; mayreviveagain. NAGAinvisibleGOLDENpeaceful23,26blocked;stepped24,24waitletpass.
BottomlooseSCROLL33,20 revealedafterLEOCROTTAcorpserot; UNKNOWNLEFT maycheckonreturnifwantIDscroll.
OBS42:17:07 healthy245skips0congestion. PublicnoteCandel7unlitexploringD43.

OLDER:
LATEST departingVLADTOP T29586 hero24,20 HP154/154 XL17/709878 AC-19 gOFF OOFF NOHUNGER nexttoolrouteDOWN.
CANDELABRUM i MAIN SEVENCANDLES UNLIT! SixfromTOP20,16attached29514+onefrom20,24attached29527;5sparecandlesBOH.
VLADTOPALL7chestschecked:20,16&20,24candlechestsEMPTY;24,16&28,24EMPTY;
28,16leftCREATEscroll,BLINDpotion,violet/yellowbrownGEMS;24,24left1504gold+BRONZEspellbook;
central24,20EMPTY tookfoodration+freshCOLDwand BOTHBOHnow.
SIXvampiresDEAD (4lords2regular). COCKATRICE20,22dead29568NOcorpse. BABYPURPLEWORM24,22dead29534corpse.
FoodMAIN E3UNC C-RATIONS (took4fromBOH ateone29529);BOHFOODrationfromcentralchest24,20.
NEWMAIN L OAKWAND UNKNOWN NEVERUSED fromtop28,16; sapphireRING fromsamechestBOH.
IDWRITEFAILED29580 markerdriesout: blankA GONE, MARKER NOW1:0 BOH (oldk) NEVERRECHARGEagain.
FOURamuletsretrievedthenstashed stillUNID: HEXAGONAL oldR=frommiddle20,24; SQUARE oldT=middle30,22;
CIRCULAR oldU=D31;BLESSEDTRIANGULAR oldb=D30. Onehex/squareLIFESAVING otherSTRANGULATION DO NOTWEARblind.
NEWBAGGEDmainEMPTYWANDS bDIG/rDIG/kSTRIKE/nSTRIKE/Ulight/Rfire;EMPTYOILLAMPj;
newP COLD fromtop24,20fresh0uses; oldd ASMO COLDnearEMPTY.
MAINWANDS NOW Bcancel0:0 S cold0:1 zcoldfresh hfireAsmo eDIG0:1 Hdig3uses Zdig7uses;
mDEATH1:5 YPOLY1:6 Jsummon0:3 VMM0:2 KcursedsLOW0:1 pSTRIKE2uses vsleep2uses;
Gtele0:1 Xtele0:8 Wtelefresh LunknownOAK. AllVladfightsmeleezerochargesused.
MAINBcancel NEVERBAG. OrbDmainalways. glevonfortravel/offstairs. BOHburdenresolvedafterrepack.
Toproute24,20W20,20N20,18E26,18S26,20E28,20DOWN.

OLDER:
LATEST VLAD TOP displayD39 T29493 hero28,16 HP133/154 AC-19 XL17/707971 gOFF OOFF noHUNGER.
VLAD DEAD29475! CANDELABRUM i MAIN (0candles) picked27,20T29479. Need7candles topchests NOTFOUNDyet.
Vladtop OFFSET17,15 ladderDOWN28,20, throne23,20,centralCHEST24,20unsearched.
Topdoors27,20;25,18;27,18;20,19;28,17 OPEN. Route28,20W26,20N26,18W20,18S20,20E24,20chest.
RemainingVampires3southniches20/24/28,24, three northonesdead (2VLORD+1V). InvisNURSEdead29447wandINVIS20,18LEFT.
XORN summonedVlad27,19dead29478. Vladfight lowestHP88, nowregen133. No wandchargesusedinVlad.
TopCHEST28,16unlockeduntrapped LOOTED blankscrollA, sapphireRING E, OAKwandL MAIN UNKNOWN.
CheststillCREATEscroll,BLINDpotion,violet+yellowishbrown gemsLEFT. Candlechestselsewhere.
MIDDLE displayD40: DOWN20,22 UP28,20. Winterwolf18,22DEAD;ICEDEVIL28,24DEAD.
MIDDLE AMULETS: HEXAGONAL from20,24→BOH oldP; SQUARE from30,22→BOH oldT. OneLIFESAVINGoneSTRANGULATION, NOTYETID DO NOTWEARblind.
BOH now58items (56+2amulets). MainfoodonlytTIN+o/qLIZARDS; lastmealrocktroll29148. Blankscrollcanusemarker1:11forIDifcostsufficient.
MIDDLErouteUP28,20W27,20N27,18(open27,19) W20,18S20,20E25,20S25,22W20,22DOWN.
MiddleMARILITH30,18ALIVEsealed;HELLHOUNDpups18,18/28,16ALIVEsealed. Waterwalkingboots24,24LEFT.
BOTTOMdisplayD41: DOWN19,20 UP22,22. MainENTRANCE31,20OPEN. Allmainmonstersdead29379 exceptTROLL30,21revivable.
BottomkillsLURKER19,24;ENERGYVORTEX19,24;LEOCROTTA33,20;REDdragon+yeti+cobra31,20;
TROLL30,21;ELVENKING29,20(armoronlyleft);UMBERHULK29,19;BARROWWIGHT25,19.
BottomSPIDER26,24alive+NAGA21,26unknown. gONnormallybutOFFatcurrentchest. Nohornconfnow.
BottomreturnUP22,22→mainroomE31,20(open)E34,20S34,24W32,24S32,26W20,26N20,24W18,24N18,20E19,20DOWND42Vlad11,23.
OBS42:09:03healthy245skipsunchanged0congestion. PublicnoteVladdefeatedsecuringcandles.

OLDER:
LATEST VLAD BOTTOM (displayD41) T29316 hero19,20 HP154/154 AC-19 XP701644 gOFF (nexttoolPg) OOFF noHUNGER.
FOUND VLAD D42 UPBRANCH11,23! Climbed29316→Vladbottom19,20. D42normalUP57,23 DOWN12,15.
Vladbottommapoffset17,15 (sourcebranch2,5→19,20). EntiretowerNOTele/NOdig walls. Centerlockeddoor31,20likely.
Sourceprimary tower.des justread: bottomladder5,7→22,22; entrance14,5→31,20locked dragon13,5→30,20.
Mayflipmapsverify. Sourcehttps://raw.githubusercontent.com/NetHack/NetHack/NetHack-3.6.7_Released/dat/tower.des
MIDDLE chestwithLIFESAVING andSTRANGULATION inrandomniches;topTWOcandlechests4d2wax+4d2tallowenough7candles.
NeedCANDELABRUM+7candles,Vladcourt. Excaldrainres,MR+reflection+freeactionunchanged.
D42lastWroute17,23S17,27E19,27N19,25DEAD;19,27S19,29W13,29DEAD.
Back17,23W11,23VLAD(branchhiddenunderheroinitially);S11,25W7,25DEADchecked29313.
D42ONLYstillunmapped17..19,y13..19 unnecessarynow. NeedSHORTCUTfromVlad11,23toDOWN12,15future!
CurrentknownVlad→DOWNridiculouslongsouthwestloopORdig northwall11,22→B11,21 withstrike, orE12,23→13,23
digN13,22→13,21 thenN13,17W11,17N11,15E12,15DOWN. OneHdigchargebest.
InventoryS cold0:1,cSHIELD+4,AC-19,foodrocktroll29148; nootherchanges.

OLDER:
LATEST D42 T29287 hero17,23 HP154/154 AC-19 XP701644 gON OOFF noHUNGER.
DOWN FOUND12,15. VLADstillUNKNOWN. MuchWmapped; remaining17..19,y13..19 and17..19,y25..29 plus11,23/25 pocket.
DISENCHANTER3,24DEAD29256; cSHIELDdrained+5→+4T29252, AC-19. Excalunchangednoeffectmessage.
S COLD FOURuses29252twice,29254,29255 now0:1. Otherwandchargesunchanged (Hdig3,pstrike2,mdeath1:5).
ZRUTY14,25dead29281corpseleft. Lastfoodrocktroll29148. LastOBS41:47:09healthy245skips0congestion.
D42WESTroute23,28SW22,29W21,29N21,24NW20,23W19,23N19,21W13,21N13,17W11,17N11,15
E15,15 (DOWN12,15) N15,13 W9,13 S9,15 W5,15 N5,13 E7,13DEADchecked;
W3,13S3,18SE4,19E5,19S5,21E7,21N7,18NW6,17W5,17DEADchecked;
back6,17SE7,18NE8,17E9,17S9,19E11,19S11,20SW10,21W9,21S9,23W5,23S5,25
W3,25N3,21DEADchecked;S3,29E5,29N5,27E9,27S9,29W7,29DEADchecked;
E11,29N11,27E15,27N15,26NW14,25W13,25N13,23E17,23CURRENT.
UNEXPLORED11,23Wfrom13,23;17,23S17,25..29;15,13E17/19,13northpockets.
BOULDERS21,23,3,19,7,17,11,21,15,25 alloriginalandbypassed. NoNEWtrapsWEST.
AdditionalWmonsters3@15,19,2@16,19,2@15,15unID alive. OriginalO8,25maybepolymorphdisench?Unknown.

OLDER:
LATEST D42 T29199 hero21,25 HP154/154 AC-20 XP700979 gON OOFF noHUNGER.
EAST ALLMAPPED NO VLAD/DOWN. WEST x3..19unknownnext.21,29N21,25N21,23unknown.
Lastfood ROCKTROLL finished29148 afterrevivedmidmeal29128killedagain29131;
leathergolem57,24dead29141 interruptedmeal thenresumed. MAINiSLIMEMOLDATE29118GONE.
Onlymainfoodlizards/tin now; BOHfoodstocks unchanged.
NEWTRAPS PIT57,25;DART69,17underB. HEROgONclearedpit.
PITFIEND70,21dead29064;HEZROU69,16dead29081;ROCKTROLL57,26dead29123,REVIVED57,25dead29131FULLYATE29148.
BlackDRAGONalivefollowing nowEhalf; 1roamer55,28unIDmaybeoriginalgargoyle; undeadwestunID.
AdditionalD42BOULDERS65,17;69,17;71,21 allbypassdiagonal. 65,25/65,27/69,29unchanged.
SEroute64,27W61,27S61,29E67,29DEADbow. Returnvia65,26bypassB65,27E69,27S69,28SE70,29
E77,29N77,17W75,17N75,15E77,15N77,13W73,13S73,19W71,19S71,20SE72,21
E75,21N75,19DEAD;S75,23W73,23DEAD. Back75,21W72,21NW71,20SW70,21W67,21
N67,17W66,17NW65,16N65,13E71,13S71,15W67,15DEAD;69,15S69,16SE70,17E71,17DEAD;
70,17SW69,18S69,19DEAD.65,13W57,13S57,15W55,15connectoriginal.
UP57,23N57,21E59,21DEADchecked;UP57,23S57,27DEADchecked (PIT57,25).
ToWEST23,28SW22,29W21,29N21,25CURRENT (21,23unexplorednext). DoNOTcrossMAGIC45,29 unnecessarily.
OBS41:40:18 healthy245skipsunchanged0congestion. No newwanduse sinceH3/p2.

OLDER:
LATEST D42 T29007 hero64,27 HP154/154 AC-20 XP699476 gON OOFF noHUNGER.
A lastmainC-rationATE28882 GONE. Nextslimemoldi orgetBOHfood. LastOBS41:34:56healthy245skipsunchanged0congestion.
D42pSTRIKE TWOuses E45,29T28950breakB46,29;N55,24T28961breakB55,23 (pwas0uses).
HdigTHREEuses now E53,29T28956opens54,29SHORTCUT avoidsMAGIC45,29 return.
D42MAGIC45,29 summoned SOLDIER44,29DEAD28949,BLACKDRAGONnow55,29alivefollowing, WRAITH47,29aliveunseen.
Blind/deafcuredax2; noHPdamage. B39,29pushedto46,29thenBROKEN.
FIVEBONEDEVILSkilled:21,20T28907(coldwandLEFT),23,16T28914+28918(two),invis23,18T28920,
59,25T28973(weaponsleft). NortheastTROLLalive;new4roamer67,18unID;2roamer65,21unID.
D42NEWroutes north55,13W21,13S21,21E23,21N23,15DEADchecked, S23,28(boulderfrom23,27pushed23,29)
SE24,29E55,29continuousDIG54,29. MAGIC45,29 avoid ifpossible.55,29N55,23DEADcheckedrocks afterboulderbroken.
55,24W54,24toexcludedstrip53 notexplored. 55,29E59,29N59,23E61,23S61,25E63,25N63,23E71,23
S71,27E73,27N73,25E75,25S75,29 (E77,29unexplored);W70,29NW69,28N69,27W66,27
NW65,26NE66,25E69,25DEADchecked;return66,25SW65,26SW64,27CURRENT Wunexplored63,27.
BOULDERS moved71,29to69,29(bypass69,28);67,27to65,27(bypass65,26);original65,25stay(bypass66,25).
SOUTHWEST x3..19 entireunknown; eastNE x65..77,y13..21 unknown; SE x61..67,y29unknown.

OLDER:
LATEST D42 T28876 hero55,13 HP154/154 AC-20 XL17/697519 gLEVON OOFF noHUNGER.
D42 UP57,23 fromD41 DOWN13,24. DOWN/VLAD UNKNOWN; MUST VLAD42 (38..41 searchednone).
Tower enclosure25..52,y15..27 and excludedstrip53. DONOTENTER, Wizarduntouched.
RouteUP57,23N57,19W55,19S55,21DEAD2greengems;back55,19E61,19S61,21E65,21N65,19DEAD;
back65,21W63,21N63,15W59,15DEAD;back63,15S63,17W55,17N55,13NOW.
UnexploredW55,13;E55,15;E57,21;S57,23.
BlackPUDDING63,18 and TWO splits62,17+63,16 DEAD28855..60; NhelmNOWCORRODED +thoroughlyrusty ACunchanged.
D42 boneDEVIL60,23roamingSE; pack23,15/21,16/23,16/23,18W; gargoyle19,18;ogre8,25;zombie15,26;
trolloriginal46,13moved65,16 alive. Centraldragons/demons/bees/moatunchanged.
D41 FINISHED noVLAD. bDIGEMPTYtested28786; HdigNOW2uses W59,29opens58,29T28786, W15,27opens14,27T28830.
OtherD41dig bW67,29opened66,29T28781lastcharge.
D41returnDOWN13,24S13,27E17,27S17,29E21,29N21,27W19,27N19,25W17,25N17,23
E21,23S21,25E23,25S23,29E77,29continuousviaNEWdig58,29+66,29. FIRE47,29/POLY61,29.
LateD41 brownPUDDING+split62,25dead28712;giantSPIDER62,25dead28714;
HELLHOUND77,20dead28744;TROLL52,29dead28791REVIVED28793alive60,29T28800;
THIRDsoldier40,29dead28801;SHOCKsphere60,29exploded28785SHOCKRESsafe,potionleft60,29.
UP14,29↔D40DOWN59,15;D41DOWN13,24↔D42UP57,23. Alloutermazeexceptexcluded53stripexplored.
FoodmainA ONEC-ration unchanged lastATE28653; newSCAREscrollBOH56items; mDEATH1:5.

OLDER:
LATEST D41 T28704 hero63,29 HP154/154 AC-20 XL17/695660 gLEVON OOFF noHUNGER.
2026-09-08 user CONTINUE; SSHpaneDEAD03:30reconnected hide/start/login credential/resume r;
SAME SAVE28421 restored. OBSstillLIVE41:08:15 checked,245skippedtotal0congestion notincreasing.
No USERSTOP, KEEP PLAYING. Calls NOWfast~1s/noescalation (permissionsdanger-full-access NEVER).
NEWMAIN H UNKNOWN DIG picked21,20D41wolfdrop28603 ZEROHEROUSES.
bDIG THREEUSES: E55,19T28505 opened56,19shortcut; lurkerescape28565; SECONDlurkerescape28700.
Zdigstill7uses,eDIG1charge,mDEATH1:5 unchanged. GlovesnowVERYBURNT+2 (fire47,29);ACstill-20.
MAIN A ONEremaining C-ration (picked2 fromsoldier58,19T28510; AoneATE28653).
NEWBOH E UNKNOWN SCAREMOSTERscroll fromsoldier58,19 picked28510 stashed28513. Bag56itemsnow.
WEST/NORTH D41 fullymapped NO VLAD; EASTpartiallymapped, remainingSE x61..77,y25..29,
farE x75..77,y13..23; littleouterstrip53,y15..27 maybeexcludeVLAD; explore.
NEXT from63,29 E65,29 thenN65,27 OR continueErow29. POLY61,29underlurkerCORPSEavoidifpossibleMRsafe.
UP14,29 DOWN13,24, VLADUNKNOWN41or42. Centralzoo x34..42insideDO NOTenter.
D41WESTadditionalroute:5,19E7,19N7,17E11,17N11,15E19,15N19,13E55,13(fullrow19..55).
9,13S9,15W7,15DEAD. Nnorthwestern3..17,13 disconnectedwall18,13.
23,13S23,14 SW22,15 SE23,16 S23,18 SW22,19 W21,19 S21,21 E23,21 S23,23DEAD.
B23,15bypass22,15; ROLLINGBOULDERTRAP23,17 createsB23,19 (bypassSW22,19).
OtherWpath22,15W21,15S21,17W19,17S19,21W15,21S15,27E17,27S17,29E21,29N21,27
W19,27N19,25W17,25N17,23E21,23S21,25E23,25S23,29 E57,29.
FIRE47,29 MUSTPASS thisrow unlessdig; web19,19underAMULET;PIT15,23;
unknowntrap15,21 found;SQUEAK21,27;ROCK19,25;ARROW23,13.
D41Eroute from57,29N57,27W55,27N55,19DEADwhitegemsbutDIG E56,19->57,19.
55,20W54,20openUNEXPLORED outerstrip (tower ends52);55,25AMULETleft;57,27GOLD.
57,19N57,17W56,17 B55,17DEADcan'tpushW54wall. No staircheckunderboulder.
57,19E63,19N63,17DEAD;S63,21W61,21DEAD,E67,21N67,19W65,19DEAD.
59,19S59,23E69,23N69,19E73,19N73,13W65,13DEAD.
71,19N71,15DEADRUSTTRAP.67,13S67,15E69,15S69,17W65,17N65,15W63,15N63,13
W61,13S61,17W59,17N59,13W57,13S57,15W55,15N55,13W23,13.
57,19S57,25E59,25S59,29E63,29current; POLY61,29.
D41KILLSnew: WOLVES6,19T28423;19,26T28463;37,13T28587;21,20T28601(dropHDIG).
INVISSTALKER16,21DEAD28450 (wasoriginalEunID15,27).
SOLDIER58,19DEAD28507(dropC-rations+SCAREcollected);femaleSOLDIER61,23DEAD28523.
THIRD soldier57,20injuredfledALIVE, last23,27tele28700.
GRAYDRAGON69,21DEAD28533corpseleft; LURKER61,14DEAD28566afterengulf28564bDIG28565.
RAVEN22,19DEAD28599;XORN32,13DEAD28621 (NOTpetoldD25).
TROLL63,20DEAD28666 REVIVED androaming2near59,20..60,23T28704.
STATUE57,24animatedBALROG28688,DEAD28692 battleaxe+whiplefthere.
SECOND LURKER61,29DEAD28701afterengulf28700bDIGescape;corpseonPOLY61,29.
YETI64,29DEAD28704corpseleft. NootherfoodsinceC-ration28653.
OtherALIVE: westTROLL revivedoriginalmagiclast5,18; westDEMON&16,17unIDnew;
COCKATRICE17,13unIDprobablypolynew (glovesON, neverbarehand).
NewCAT65,17unknownnotpet; CAT49,16insidetower;giantSPIDER41,13new.
OuterSE giantSPIDER61,27, WOLF73,27, 4roamer72,27unID now,1@62,25/27.
Allcentralzoo untouched. NoVlad yet.

OLDER:
LATEST D41 T28405 hero16,13 HP154/154 AC-20 XL17/692522 gLEVON OOFF noHUNGER.
MESSAGE 'You find a spiked pit. >>' clearedSPACEpending. SPIKEDPIT15,13underprojectiles.
UP14,29 DOWN13,24 veryclose. VLADUNKNOWN D41or42. ONLYWESTx3..17mappedmost +row13to16.
Centerx34..42zooDONOTENTER (manycockatricesetc). HeroMR/freeaction/reflection/halfphysunchanged.
Zdig7HEROUSES lastW17,19D41T28321 OPENwall16,19 ->15,19 safeavoidMAGIC15,17.
D41TRAPS MAGIC15,17(undergold) &3,15(undergold) spawnedmonstersblind+deaf; STATUE3..7,21createdAIRELEMENTAL;
WEBsomewhere7,21..27(maybeunderettinmummycorpse7,27), SPIKEDPIT15,13.
D41kills PANTHER17,17;TROLL16,17killed28308 revived28320thenDEAD6,29T28359againREVIVABLEleft;
VAMPIREinitialbat16,17DEAD28317 (noexpforbat form);HORSE16,17DEAD28318;
ETTINMUMMY7,27DEAD28362corpseleft;AIRELEMENTALengulf3,21DEAD28373 HP135nadir;
REDDRAGON3,14DEAD28384corpseleft;DUSTVORTEX3,15DEAD28381;IRONPIERCER4,15DEAD28382;
QUASIT3,16DEAD28386;ZRUTY3,16DEAD28390 corpseleft.
THREEGREYELVES12,13(twofriendlyfiredead),16,13lastDEAD28403. Noelflootrecoveredyet.
AlltemporaryBLIND/DEAFcuredhorn aftertrapfights. NofoodsinceOLOGmealD40T28185.
UNIDENTIFIEDELEMENTALinitial15,27 now17,21alive; bats/dogscreatedMAGIC15,17 somealive around19..23,19..23.
UntouchedoriginalfarEelfpack+wolfpacks+troll alive. NoMINOTAURseenoutside.
WESTroute UP14,29W13,29N13,19W9,19S9,21E11,21DEAD;back9,19E15,19N15,17W13,17DEAD
E17,17S17,19DEAD(nowDUGW16,19to15,19);UP14,29W11,29N11,23W9,23S9,29W3,29N3,27E5,27N5,23
W3,23S3,25DEAD;back3,29E7,29N7,21W3,21N3,13E16,13current.
UNMAPPEDwest:9,13S9,15 and remainingx5..11,y15..19; northrow13E16+allcenteroutsideE18.
LootAMULET13,17;POTION9,19;GOLD13,21/15,17/3,15/5,21/9,23;corpseslisted;elfweapons11/12/15,13.
OBS36:11:52healthy0drops. PublicnoteD41search AI GPT6Astraupdated.

OLDER:
LATEST D41 T28279 hero14,29UP HP154/154 AC-20 XL17/690113 gLEVON OBLINDFOLDON.
UP14,29<->D40DOWN59,15. DOWN/VLADUNKNOWN. InitialteleCENTERMASSIVEZOOx34..42,y18..24 INSIDETOWERavoid.
OUTSIDE E15,27 elementalunIDnearhero; elves7,15/9,14/11,13; B37,13bat; d59,15/16/17/60,17wolfpack;
t65,16trapper?;T69,19troll;elves65/67/68,23+69,22;d75/76/77,27+69,29secondwolfpack.
No outsideMINOTAURorDRAGONseeninitial. Don'tentercentralenclosure.
D40 FULLYSEARCHEDNO VLAD. So entranceD41OR42 only. Allouterfloormapped(exceptbouldercovereddeadends11,29/61,21).
D40 FINALresources Zdig6HEROUSES (lastW69,25T28264+W63,25T28268)
openedwall68,25+62,25, row25eastshortcutnowthrough61..71. bDIG0uses mDEATH1:5 eDIG0:1 vSLEEP2uses.
NEWMAIN p UNKNOWN STRIKING fromROCKTROLL74,23 picked28230, 0HEROUSES trollused2chargesminimum.
SECOND OLOGHAI74,23DEAD28225, ROCKTROLLsame74,23DEAD28227 BOTHREVIVABLEcorpsesleft.
At28263 OLOGREVIVED4@74,19;rocktrollfateuncertain. Loot74,23CYANpotion+SPLINTMAIL+blue/orangegemsleft.
OnlyD40lootrecoveredpSTRIKE. Ologfirst67,21fullyate28185. Statue66,23unknown1last71,20alive.
D40upperfarEroute69,21E71,21N71,17E73,17N73,15W71,15N71,13E77,13S77,19W73,19S73,22
SE74,23NE75,22N75,21E77,21S77,25W73,25S73,27W69,27S69,29E75,29N75,27E77,27S77,29DEAD.
Deadspurs75,19N75,15;71,19W69,19;69,27N69,25E71,25N71,23DEAD.
B73,21pushedS73,23;B75,23fixed; bypass73,22SE74,23NE75,22.
ReturnfromfarSE nowDUG row25x68+62 through, traveltoDOWNworks from63,25.
OBS35:45:01healthy0drops~7minago.

OLDER:
LATEST D40 T28191 hero69,21 HP154/154 AC-20 XL17/689442 gLEVON OOFF noHUNGER.
66pendingeasttoward71,21. EASTONLYx>70unmapped. WEST/SOUTH/61..69allmappedexcepttinyfarEconnections.
D40eastmaze route55,21E59,21S59,23E61,23S61,25W59,25S59,27E61,27S61,28
SE62,29E67,29N67,25W63,25N63,20NE64,19E65,19N65,17W63,17N63,15W61,15N61,13
E69,13S69,17W67,17N67,15W65,15DEAD;back67,15S67,21W65,21S65,23E69,23N69,21current.
SOUTHdeadspur63,25S63,27E65,27DEADchecked;61,15S61,20DEADboulder61,21againstwall.
BOULDER61,29(HILLGIANTdrop) bypassNW61,28from60,29thenSE62,29.
BOULDER63,21pushedN63,19nowagainstwall, bypass63,20NE64,19.
WEB63,21underAMULET63,21; newANTI65,29. STATUE66,23animated28190 unknown1still66,23.
HILLGIANT61,29DEAD28085;3WOODLANDELVESDEAD67,26twice+66,25;GREENELF63,24DEAD28104.
MOUNTAINCENTAUR69,14DEAD28138;GIANTZOMBIE69,16DEAD28142;LIZARD68,17DEAD28144corpseleft.
OLOGHAI67,20DEAD28155, summonedEARTHELEMENTAL67,20DEAD28157.
OLOGcorpseate28161 revivedMIDMEAL28165to67,21 KILLEDAGAIN28168 FULLYATE28185 NOREVIVE.
NoHUNGERstill, nootherfoodused. CREATEwand67,20leftfromolog; noD40lootcollected.
OtherALIVE4roamer71,24unknownprobablytroll;3@75,22unknown;statuecreature66,23unknown1.
Allresourcessameprevious Z4uses, v2uses, k/n/rEMPTY, mDEATH1:5 eDIG0:1 bDIG0herouses.
MajorD40returnsnewdig5,18; southrocks23+24,29 open. UP10,25 DOWN59,15 NO VLADYET.

OLDER:
LATEST D40 T28043 HP154 noHUNGER gLEVON OOFF, longreturnbatchanimationwaitGETSCREEN.
AllWESTandSOUTHmappedNO VLAD; ONLYfarE>60unmappedaccessible55,21E.
WESTPOCKET5,19E11,19DEAD,5,21E15,21DEAD; Zdig4thuseS5,17T28006 openedwall5,18.
WESTBLUE DRAGONalive(notminotauranymore)9,22last28021; petkitten7,19followingthenunclear, weapon7,19appeared28043.
Southroute55,21S55,27E56,27SE57,28S57,29W11,29DEADboulder11,29left.
BOULDER57,27bypassSE56,27. B29,29pushedto24,29whereB23,29blocked; BOTH BROKENnSTRIKE27949.
nSTRIKE NOWEMPTY0:0; kSTRIKEtested27948EMPTY0:0 (fourpriorusesonly).
SouthBEAR19,29; gems17,29 rocks23+24,29; corpses53/57,29;weapon43,29left.
WARGpack5TOTALDEAD, final58,19/54,20/56,21. XL17/687495.
GoodNEWUP->DOWNrouteUP10,25W9,25N9,21W5,21N5,17(newdig)E13,17S13,19E17,19N17,17E23,17N23,15W21,15N21,13E54,13SE55,14S55,16SE56,17E57,17N57,13E59,13S59,15DOWN.
OBS35:17:51healthy ~10minago CHECKSOON.

OLDER:
LATEST D40 T27913 hero59,18 HP154/154 AC-20 XL17/687042 gLEVON OOFF noHUNGER.
DOWN59,15 confirmed. PURPLEWORM59,16 killed27910 after engulf27907 and Zdigescape27909.
Zdig now3HEROUSES; vSLEEP2HEROUSES lastS59,15wormHITbutRESISTEDsleep27906.
WARG58,19adjSW F1x4pending; twoearlierwargsdead59,14+59,17.
VladTHISRUNrangeD38..42 confirmed dungeon.def Gehennom9..13+ValleyD30.
D38/D39fullysearchedNONE; D40/41/42remain. Vlad CANspawnoutsideWizardtowerconfirmed yendor.des.
D40northernroute33,13E54,13 (boulder45,13pushed55,13), SE55,14 S55,16 SE56,17 E57,17 N57,13 E59,13 S59,15DOWN.
Boulder55,17bypassedSE. FarE>60 andsouthrow29E9stillunmapped; west5..11,19..21smallunmapped.
FormerwestMINOTAUR nowDRAGON5,20 tele27904 likelypoly7,15, identityunknown.
WhiteDragon31,17INSIDE; Wizard41,20ASLEEPavoid; peacefulfiregiant34,22inside.
PETKITTEN19,15last27904alivefarbehind. Otheroutermonsters hillgiant59,27,centaur71,17,elf63,23,troll71,29; wargsroam.
Purplewormcorpse59,16left. NoD40lootcollected. OBS35:17:51healthy0drops.

OLDER:
LATEST D40 T27877 hero33,13 HP154 AC-20 XL17/686126 noHUNGER LEVgON OOFF.
E8justsentfollowingrow13. UP10,25<->D39DOWN43,24. DOWN/VLADUNKNOWN.
WIZARDTOWERTOP centerWizard41,20confirmedtelepathy DO NOTengageyet beforeVlad+routebottom.
MINOTAURwesternroamerALIVE last9,24around27853; SLEEPvreservedforhim v1herouseunchanged.
WHITEDRAGONinitial26,25now30,17ALIVE. HEZROU31,19ALIVE.
PEACEFULFIREGIANT34,24 don'tattack; ICEDEVIL35,25alive; VROCK53,25alive.
OtherinitialunknownDEMON47,22; TROLL77,21; centaur61,14;worm59,16;elf60,29;
wolfpack38/41/42/43,29; centerWizardguarddogs/eelsinsideenclosuredon'ttouch.
NEW PET TAMEKITTEN14,15tamed27834withTHROWNfoodrationT(mainTgone). Last16,13at27847following
butnowfarbehind; don'tforceattackcats. OldinvisXORNpetD25stillnotseen.
BROWN PUDDING15,26+2splitsALLDEAD27795corpse14,25left. MainarmorconfirmedUNCHANGED27889?actually27789.
SluggishmessagefromANTIMAGICnotbootsproblem. TRAPS ANTI15,27(undergold),3,27,3,19;
POLY7,15 &27,13(MRsafe). Hairneckwarning13,27unIDtrapgemunder.
BOULDERS19,21;21,23; former13,15pushedto18,15thenDESTROYEDkSTRIKE27839.
kSTRIKE now4HEROUSES(lastE17,15D40), rDIGEMPTY0:0, Zdig2HEROUSES(lastW9,13D40throughwall8,13).
ZfirstuseW59,23D39. bDIG0herouses. mDEATH1:5 eDIG0:1 YPOLY1:6 allsame.
D40 exploredSWWESTroute UP10,25E11,25DEAD; W9,25N9,21E15,21DEAD;
W11,21S11,23E17,23S17,25E21,25N21,24NW20,23W19,23DEADboulder21,23;
E20,23SE21,24S21,25W17,25N17,21E18,21NE19,20N19,19E23,19DEAD;
W21,19S21,21E23,21S23,27W15,27(ANTI)N15,25W13,25S13,27W7,27DEAD;
E9,27S9,29W3,29DEAD;E5,29N5,27W3,27(ANTI)N3,25E7,25N7,23W3,23N3,13(ANTI3,19);
E7,13S7,15(POLY)E19,15(boulderbroken18,15)N19,13W9,13DEAD;
DIGW9,13shortcutto7,13 W5,13S5,17E13,17S13,19E17,19N17,17E23,17N23,15W21,15N21,13E33,13current.
Unexploredturns5,19..21 (minotaurpath);23,27S23,29 onwardS/E; upperrow13E33onward;
everythingeastof24exceptrow13unmapped. Deadend15,17checked.
LootleftAMULET5,23;TOOL7,25;GOLD3,21/15,27/21,15;GEMS3,25/7,13/13,27/17,13;
rocks17/18/19,15;CORPSE21,25unknownleft. NoD40lootcollected.
OBS34:51:59healthy~10minago. NOUSERSTOP KEEPPLAYING.

OLDER:
LATEST D40 T27747 hero10,25UP HP154 AC-20 XL17/685955 noHUNGERnotSATIATED. gOFF.
UP10,25<->D39DOWN43,24. DOWN/VLADunknown. POjustsentforinitialteleinspection.
D39 FINISHED ALLFLOORmapped NO VLAD. Newstrong5@37,19unIDALIVEleftbehindwall38.
D39 OLOGrevivedALIVEUParea+new4+multiple1/2. PYROLISK13,14aliveNW, fewothersalive.
D39 finalresources: rDIGEMPTY tested27648; SIXsuccessfulHEROUSES total (lastE49,23D39).
Z UNKNOWNDIGfromGREYELF4,24 ONEHEROUSE W59,23T27649 openedwall58,23.
b UNKNOWNDIGsameELF0HEROUSES. Deathm1:5 vSLEEP1herouse YPOLY1:6 eDIG0:1 unchanged.
FOODUNCHANGED noD39foodafterwhiteDragon27203. Satiationended27633.
D39 newkills 4WARGS east72,23/73,23/72,21/70,19; SNAKE72,23; WARHORSE64,23.
BARBEDDEVIL56,23dead27651 ARMORleft. COCKATRICE51,23dead27655 NOCORPSE.
Oldcockatrice46,23+RAVEN45,24corpsesROTTED; armor46,23now.
WEB15,17(disentangled27712) weaponcovers. Wrench18,15unknowntraplikelyleveltele.
D39 TWO DIGshortcuts wall50,23 +58,23 nowpassable.
GoodUP->DOWNroute63,17E71,17S71,23W43,23(useBOTHdigshortcuts)S43,24DOWN.
UP->DOWNreverse43,24N43,23 E71,23 N71,17 W63,17UP. AvoidSQUEAK70,17 harmless.
OtherD39knownTRAPSlevelTELE26,21;TRAPDOOR35,24;FIRE45,14/42,18/22,26;
ARROW16,26;POLY72,14 &71,27;PIT54,15;SQUEAK70,17.
NewlootTOOLS66,25unknown left; WOODENring67,27left. Mostcorpsesdecaying.
OBSlast34:29:23healthy~10minago. USERNO STOP KEEPPLAYING.

OLDER:
LATEST D39 T27590 hero43,21 HP154 AC-20 XL17/684785 SATIATED LEVgON OOFF.
DOWN FOUND43,24! UP63,17. VLADstillunknown checkingremainingeasternpocketsbeforeDESCEND.
NewDIGshortcut49,23E->51,23 throughwall50,23 r6thherouse27573 (firstD39).
NewmainZ+DIGb UNKNOWNdigwandsBOTHfromGreyelf4,24picked27409;0HEROUSES each.
Greyelf4,24DEAD27406 STRIKEwandleft there; bothants+giantspiderdead27405.
Succubus15,15DEAD27445 POTION15,15left. WRENCHINGtrap18,15undergoldunknown(probtele).
GREENELVES37,19+33,21DEAD27508lootLEFT. GARGOYLE21,21dead27518corpseLEFT.
ORCMUMMY19,18dead27521mummywrapLEFT. SPIDERwest17,19lastALIVE.
OLOGrevivedUPNWloopALIVE +unknown2+two1s separatedbywall20noimmediatethreat.
NEWtrapsLEVELTELE26,21(MRprevented27514), ARROW16,26. Othertrapsolderentries.
MostWEST/NORTH/CENTRALmapped noVlad. RemainingWEST row17x7..17; row21x7..15;
row25x10..12; x37y23..27; CENTRALx33y17..19; EASTbottomrow25x47..49;
Eloopsx57/61y21..27; UPErow19x67..71; FARSE65..71y21..25.
DOWN43,24 underheropassedN27588 confirmedstairdisplayafterleaving. Raven45,24,COCKATRICE46,23.
RouteDOWN->UP potential43,24N43,23 E51,23(newDIG) N51,21 E59,21 N59,19 E63,19 N63,17
BUT wall58,21 and58,20? inspect whenusing. Existinglongrouteearlier.
NewestWESTroute3,24N3,13E27,13S27,17 N27,15W5,15S5,19E17,19S17,23W9,23S9,25
W7,25S7,27E15,27N15,25E35,25N35,21N35,17E37,17S37,21W19,21N19,17E31,17N31,15
E39,15S39,19E41,19N41,13 (Ewall42) S41,17E43,17N43,15E47,15S47,21SW46,22W41,22
S41,27W39,27N39,21E49,21S49,23 DIGE->53,23N53,21S53,27W43,27N43,21current.
OBS34:29:23healthyzero drops/congestion/reconnect. PublicnoteDOWNfound/AIcurrent. NOUSERSTOP.

OLDER:
LATEST D39 T27405 hero3,24 HP152/154 AC-20 XL17/684123 SATIATED LEVON OOFF.
GREYELF4,24 hostile adjacentE (D38escape STRIKE+DIG), F6F6F6 justsent inspectresult.
GIANTSPIDER4,25dead27403 corpseleft; BOTHsoldierantsdead27405. Otherinitialspiderunlocated.
PITFIEND25,19DEAD27364 weaponleft. HELLHOUNDPUP43,18DEAD27341 corpseleft.
WESTROUTE from45,22 N45,21 E49,21 N49,13 W43,13 S43,19 W39,19 N39,13 W31,13
S31,19 W19,19 S19,23 E35,23 S35,27 W3,27 N3,24current. DOWN/VLADstillunknown.
TRAPSnew FIRE45,14; FIRE42,18; TRAPDOOR35,24(LEVcrossed); FIRE22,26.
LootleftARMOR30,19 &28,22, GEM32,19 &33,23, WEAPON25,19, GOLD7,26.
Needexplorefarwest3..17,y13..25; innercentralroomgaps33..37/45..47,y15..19;
alsoSEroominterior65..71,y23..25. UPNWloopOLOGrevivedalive+unknown2 last53,18.
ResourcesUNCHANGED mDEATH1:5, vSLEEP1herouse, rDIG5herouses(noD39dig).
OBS34:14:32healthyzero drops/congestion/reconnect. USERNO STOP KEEPPLAYING.

OLDER:
LATEST D39 T27325 hero45,22 HP154 AC-20 XL17/683242 SATIATED LEVgON(since27303). OOFF.
UP63,17 DOWN/BRANCHunknown. Exploringwestthrough45,22north. NoSTOPUSER keepplaying.
MINOTAUR67,13DEAD27260 after vSLEEP E63,13T27255 ->5Excalhits NOdamage.
vSLEEP NOW1HEROUSE (D30wand originally0uses). minotaurMR0/nosleepres confirmedprimarymonst.c.
Deathmstill1:5 Ypoly1:6 eDIG0:1 rDIG5herouses(noD39digused).
BONEDEVIL steppedPOLY72,14->OLOGHAI27260; killed67,14T27269 REVIVED nowT52,19ALIVE27325.
Othernewwarning2@53,18 unknown. OlognearUPwestloop, don'tassumedead. AllotherinitialD39monstersbelow.
RAVEN45,24DEAD27315 corpseLEFT; itsBLINDNESS curedax27316.
COCKATRICE46,23DEAD27320 CORPSELEFT DONTTOUCH/EAT (giantbeetlecorpseontopnow).
QUASIT45,23DEAD27322 noCORPSE. GIANTBEETLE46,23DEAD27325corpseleftovercockatrice.
Revieweronce falselyrejectedmoveN45,25 saidcockatricecorpse45,24. VerifiedfarlookexplicitRAVENCORPSE,
thenSAMEactionapprovedafterread-onlyproof. Resolved, noactiveblock. Sightedglovedlevitating.
D39ROUTE: UP63,17 W59,17 N59,13 W51,13 S51,19 E57,19 N57,15 E59,15 S59,17 E73,17
N73,13 W63,13 (MINOTfight67,13) S63,15 E73,15 S73,27 W63,27 N63,21 W59,21 S59,27
W55,27 N55,21 W51,21 S51,27 W45,27 N45,24 N45,22current. (route45,27notactuallyvisitedbutpassable)
UnmappedmajorWESTx3..49, and east-room interiorloweredges somerows19/23/25unseenpossibleSTAIRS.
TRAPS SPikedPIT54,15; SQUEAK70,17; POLY72,14 &71,27. LevON avoidpits+holes.
LOOTgold55,17(39),62,23; WOODENRING67,27; ARMOR55,24uninspected; allLEFT.
MINOTcorpse67,13LEFT, OLOGoldcorpse67,14GONErevived; WHITEDRAGON66,17ATE27203 nofoodmainused.
PITFIEND25,19sleepingALIVE. GREYELF17,19ALIVE(fromD38hasSTRIKE+DIG);
SPIDERS15,18+16,21alive,ANTS16,20+17,23alive. OriginalTROLL24,26teleNOTSEEN27316 maybewanderingfarleft.
OBS33:50:31healthy0drops approx10minago. NoteD39/3rulersdeadAIcurrent.

OLDER:
LATEST D39 T27244 hero71,17 HP154 AC-20 XL17/681933 SATIATED. UP63,17<->D38DOWN69,17.
D39 DOWN/BRANCHUNKNOWN. gOFF OOFF. WandresourcesUNCHANGED sinceD38: m1:5 e0:1 r5herouses Y1:6.
vSLEEPwandunused0herouses, planuseonMINOTAUR (primarymonst.c confirmsMR0+nosleepres).
MINOTAURALIVE67,21 currentlybehindwall20 cannotreachhero yet. BONEDEVIL68,25ALIVE.
PITFIEND25,19sleepingALIVE. COCKATRICEroamer49,20ALIVE; avoidtouchcorpse.
GREYELF17,22ALIVE likelyescapedD38hasSTRIKE+DIG. Troll24,26alive;
spiders15,17+17,19,ants17,20+17,21,imp49,17,bat49,18 alive (oldtelecoords).
GELATINOUSCUBE61,17DEAD27151corpseleft.
WHITEDRAGON66,17DEAD27157, ATEWHOLE27203 duringHUNGRY ->SATIATED; fullHP. Nofoodinventoryused.
D39 SPikedPIT54,15 fall+escape27237 HP1lossFULLrecovered. SQUEAK70,17 triggered27244.
MappedwestUPloop: UP63,17 W59,17 N59,13 W51,13 S51,19 E57,19 N57,15 E59,15 S59,17 E71,17current.
Loopinteriorsinspectedrow15+17, lonewall54,16. Gold55,17LEFT. No stairsinloop.
Eastnewexplorationfrom71,17; likelyopensN71,16 andE72,17. Boundarieslevelx?y12..28.
OBSlast33:34:57healthy0drops approx12minago. PublicnoteD39/3rulersdead/AI.
D38 FINISHEDNO VLADbranch(allmajorfloorchecked); final63,19..16connectionCONFIRMEDpassable.
D38 dwarfMUMMY64,13dead27140corpseLEFT. Down69,17 UP35,20 fastestroutepreviousentry.
USERNO STOP KEEPPLAYING. No stopmessage, onlydateenvironmentupdateSep8.

OLDER:
LATEST D38 T27134 hero68,17 HP154 AC-20 XL17/681090. DOWN69,17FOUND! UP35,20.
CheckingFINAL NEleftedge63..64,y13..19forVLADbeforeDESCEND. Othermapmostlyfullyexplored NOextraUP.
NEWtraps FIRE68,24 avoid; UNKNOWN46,22; LEVELTELE57,14; TELE70,14; RUST18,23; HOLE17,24.
BOULDER68,16pushedfrom68,17T27134. Boulders40,17/51,17/53,18/4,14/17,14/17,16/12,23.
D38BEST UP->DOWNroute: UP35,20 NE36,19 N36,16 (DUG36,17) E61,16 S61,19 E63,19
N63,16 E67,16 SE68,17 E69,17DOWN (63,19..16abouttoinspectunknown).
ALTERNATE known:35,20->36,18 N36,16 E61,16 S61,21 E66,21 N66,13 E71,13 S71,17 W69,17DOWN.
DIG r NOW5HEROUSES (N20,23D38;W53,19D38T26969;N36,18D38T27002 plusD35/D37).
mDEATH1:5 eDIG0:1 YPOLY1:6 unchanged. gOFF OOFF nofoodconsumed NOUTHUNGRY.
ICEDEVIL52,19DEAD26973; HEZROU43,20DEAD26979; TITANOTHERE38,23DEAD26992corpseleft.
WINGEDGARGOYLE35,18dead27002 HP145nadirFULLRECOVERED. NAZGUL48,20dead27111 sword+TOPAZringleft;
NAZGULBREATHSLEEP reflected, notwand. SOLDIERANTstatue25,22animated27074 killed26,23T27075corpseLEFT.
VRock55,15sleepingalive; LONGWORM29,15sleepingalive; z30,16unIDalive; small1@63,13aliveunID.
WholeWandcentral+SEfloorchecked forstairs. OnlyNEleftedge63,13..19unseen. NoVLADyet.
TOWEL39,15left; gold38,16+25,16left. PublicnoteD38/3rulersdead unchanged.
OBS33:14:00healthy0drops approx10minago. USERNO STOP KEEPPLAYING.

OLDER:
LATEST D38 T26966 hero56,18 HP154 AC-20 XL17/679104. DOWN/BRANCHstillUNKNOWN.
mDEATH1:5 YPOLY1:6 eDIG0:1 rDIG3HEROUSES(latestN20,23D38T26863). gOFF OOFF.
North/SW/Eouterloops mapped. D38 UP35,20. No stairs other thanUP seen.
NEWTRAPS RUST18,23; HOLE17,24underelfCORPSE (elfdigescape26857toD39ALIVEhasSTRIKE+DIG);
LEVELTELE57,14; TELE70,14. Avoidall. Noothernewgear/damage Wi13.
D38addedroute11,21 N11,13 W3,13 S3,21 E6,21 N6,16 E8,16 S8,24 E20,24N20,23.
DUGN20,23through20,22 ->20,21 N20,18 W14,18 N14,13 E61,13 S61,21 E66,21
N66,13 E71,13 S71,26 W48,26 N48,23 E56,23 N56,18 current.
Remainingunmapped CENTRAL x24..56,y15..24 and smallinnerW/S/Eedges. FARrightx73+unseenwall72.
KilledEARTH11,18(115goldleft), IRONPIERCER7,16(corpseleft), QUASIT19,21, GIANTBEETLE20,19,
WOODGOLEM19,18quarterstavesleft. GREYELF17,24killedbyotherelfSTRIKE; secondelfescapedD39.
GREYELF50,24dead26956lootleft. HELLHOUND51,23dead26960, underlyingBANDEDMAILleft.
VAMPIREBAT53,13dead26906corpseleft; COBRA52,13statueanimatednear42,13 dead26909;
DUSTVORTEX52,13dead26910. FullHP noongoingstatus.
VRock55,15sleepingaliveidentifiedfarlook. HEZROU43,20alive. Othermonster4@51,19unidentified.
LONGWORM29,15sleepingalive. Small1roamerwestcentral46,23 alive. Demon68,15initialnowunknown.
Gold25,13/60,13/53,26/56,24left; WOODENRING28,13left; gems19,14+30,14left.
OBSlast33:01:17healthy0drops about8minago. USERNO STOP KEEPPLAYING.

OLDER:
LATEST D38 T26819 hero11,21 HP148/154 AC-20 XL17/677747 Wi13. UP35,20. DOWN/BRANCHunknown.
gOFF OOFF lampEMPTY. mDEATHnow1:5 (TWOminotaurs34,23+39,23 killed26765).
Firstminotaur hit hard154->107, recovered searching with blindfold. EttinZ33,22dead26783.
Ochrejelly10,20DEAD26819 acid6damage corpseLEFT. Boulder12,23 pushedfrom11,23.
Exploringnorthvia11,21. Nearbywarning3@11,17 /1@7,16 /1@14,21.
D38route UP35,20 S35,26 W28,26 N28,23deadend; returnE33,23 N34,18 W23,18
S23,26 W3,26 N3,23 E11,23 N11,21 current. Openingnorth8..11,22. EntireSroomdeadends.
HEZROU43,20alive; demon55,15+68,15unidentifiedalive; longworm29,15alive.
Elves43..48,20..23/dog48,24/imp21,20 alive. No traps yet. FoodT1rationmain nothungry.
Othergear/resources unchanged eDIG0:1 rDIG2herouses YPOLY1:6 WfreshTELEmain UemptyLIGHTmain.
OBS32:48:25healthy0drops. NoteD38/3rulersdead. USERNO STOP KEEPPLAYING.

OLDER:
LATEST T26747 D37 hero14,17 HP154 AC-20 XL17/676272. DOWN15,13found26651.
ABOUTTOtravel_.thenDESCEND. gOFF OOFF jEMPTY. USERNO STOP KEEPPLAYING.
D37WEST+SOUTHWESTextensivelysearched NO VLADbranch. Still FAR EAST S72,24andE73,18UNEXPLORED.
MainrouteUP72,18 ->S72,23 W55,23 S55,27 W51,27 N51,21(MAGICavoidvia50,22)
W47,21 S47,27 W27,27 N27,13 W23,13 S23,19 W19,19 N19,13 W15,13DOWN.
Allothernorth/center/westloopsdeadendsnostairs; DIGSHORTCUTW39,18through38,18T26614 usingr2ndherouse.
D37SQUEAK55,19 ARROW25,13 RUST4,23 MAGIC51,21.
MINOTAUR4,16DEAD26663corpseLEFT. WARHORSE15,17DEAD26747corpseLEFT.
ELFLORDS47,18/47,17/47,19dead26597/98/26600; CARNAPE52,18dead26593corpseLEFT.
RUSTMONSTER34,23dead26620; ETTIN32,23dead26624corpsesLEFT.
GREYELF7,14dead26677, ELFLORD5,15dead26679, GREYELF5,16dead26681,
GREYELF5,18dead26684; lootleftallNW. Nofood36,17ANYMORE (eaten/pickedupmonster) checked26616.
WANDUlightEMPTY0:0MAIN; WandWnewTELEunknown0herousesMAIN. Otherallgear/resourceunchanged.
rDIG2herouses S25,15D35 +W39,18D37. eDIG0:1. mDEATH1:7 YPOLY1:6.
Goldleft3,23/10,21/12,24/11,19/16,15/21,18/31,17/33,24/45,14. Gem29,24.
UNENGAGED YETIwestroamer andOGRE64,23+creaturet66,21magicspawnEareaalive.
OBSlast31:55:45healthy0drops (approx15minago now). NoteD37/3rulersdead.

OLDER:
LATEST T26590 D37 hero55,19 HP154 AC-20 XL17/673732 NOTSATIATEDnow(NOTHUNGRY).
WNEW TELEPORTunknown0uses MAIN from56,24T26518. UoldLIGHTextractedMAIN26507,
USED3charges65,23T26508/56,27T26520/42,25T26544, NOWEMPTY0:0 at37,13T26568.
Otherwand/equipmentunchanged eDIG0:1 mDEATH1:7 YPOLY1:6 rDIG1herouse. gOFF OOFF.
D37UP72,18.DOWN/BRANCHunknown. Snake72,19DEAD26493; Woodlandelf71,20DEAD26496
armorloot71,20and71,21LEFT. XORNS67,22dead26502 and64,23dead26507corpseLEFT.
EARTH ELEMENTAL51,25dead26527. MAGICTRAP51,21trigger26531 summonedOWLBEAR50,21
killed26532corpseLEFT; blindness/deafcuredax26533. OGRE+creaturetspawnedE64,23/66,21alive.
YETI33,26hit26548FLED currentlywest28,27alive. OtherYETI2@51,19approaching.
3humanoids@43,14initialroamingcenter40..55,18..23NOTFOUGHT unID.
D37mappedrouteUP72,18 via72,20S72,23 W55,23 S55,27 W51,27 N51,21(magic!)
W47,21 S47,27 W31,27 N31,21 E37,21 N37,17 W31,17 N31,13 E61,13 S61,19 W55,19.
NORTHloopsmaybedeadend, WESTFORK30,25leftUNEXPLORED toremainingleftmap.
OtherforkS72,24notexplored. Foodration36,17LEFT;gold31,17+45,14+33,24left;
BOULDER32,26avoid. SQUEAKsomewhere55..60,19 encountered26590. MAGIC51,21avoidreturnvia50,22.
OBS31:55:45healthy0drops. PublicnoteD37/3rulersdead. USERNO STOP KEEPPLAYINGLIVE.

OLDER:
LATEST T26489 D37 UP72,18 HP154 AC-20 XL17/672874 SATIATED. gOFF OabouttoON.
D36DOWN10,23 ->D37UP72,18. NO VLADbranchseenD36 (fewwateredgeareasunexplored).
D36route UP71,19 SW70,20 W43,20 N43,17 W13,17 SW9,21 SW7,23 W5,23 E10,23DOWN.
LEVONALLswamp, removegonlyonDOWN10,23. Shortcutrow20haspuddingsavoidviay17.
BAALDEAD26375, JUiblexDEAD26389, allD36bossesdone. eDIG0:1 afterJuiblexexpulsion.
D36ochreJELLY42,17dead26413, jellyfish26,17dead26423, ants22,17+19,18dead26426/30.
MARILITH5,23dead26440 dropped64goldLEFT, LunknownVENZAR+PunknownTELEscrolls BOTHBAGGED26443.
BLACKLIGHT5,26EXPLODED26453 causedHALLU curedax26456, noresource/equipotherchange.
HILLGIANTS3presenthostile west roaming, grayUNICORNhostile+YETIwestalive. Brownpudding42,21alive.
1lastlemure60,20alive. Boulders3,26+6,23pickedupgiants,0@20,17remains.
SLEEP11,17 under481goldLEFT. SQUEAK5,21. ANTIMAGIC59,20. Potions21,17+37,16LEFT.
Down10,23visibleaftersteppingoff, nohiddenitem. Westdry5,23gold and3,25goldnostairs.
OBS31:28:37healthy0drops. PublicnoteBaal/Juiblexdead(swampD36outdatednowD37).
USERNO STOP KEEPPLAYINGLIVE.

OLDER:
LATEST T26389 D36 JUiblexSWAMP hero69,20 HP137 AC-20 XL17/672319 SATIATED levON.
BAALZEBUB DEAD72,18T26375 after7ExcalhitsfromUP71,19! Nochargesused.
CLAYGOLEM72,19dead26379rocksleft. BLUEdragon71,21dead26385CORPSELEFT.
JUiblexENGULFED69,20T26386, sickCUREDax26387, DIGe6T26388expelledsetHP1,
POtelelocated70,19, F9KILLEDJUiblex26389! NOsicknessremaining. eDIGnow0:1.
Juiblexpoisoncloud70,19..21 obscuredhim, resolvedbyteleblindfold. Health129nadirthen137.
D36UP71,19, DOWNexpectedfarwestx1..11. SWAMPWATER levgONkeep.
Otherwarning5@70,24 MINDLESSdangerunidentified, demon5,23unidentified farW.
3lemures60..62,18..20 approach. HeroabouttoRO444 west69,20->66,20.
OBS31:16healthy. PublicnoteBaalANDJuiblexdead. USERNO STOP LIVEKEEPPLAYING.

OLDER:
LATEST T26371 D36 UP71,19 HP154 AC-20 XL17/668376 SATIATED BLIND Oon gOFF jEMPTY.
BAALZEBUB LURED FROM D35down73,21 toD36T26369, ALIVE fightingadjacentUP71,19.
LastBaal72,18, F9attackpendingnexttool. HOLDUPSTAIRS, blindfoldblocksSTUNgaze!
D35BAAL laircomplete, UP12,19 DOWN73,21. BAALleftD35, horned61,20/barbed67,22stillaliveasleep.
D35 KILLED minotaur16,17, vampires19,20x2, greenSLIME20,25 (RlastFIRE26274 now0:0),
cockatrice25,18CORPSELEFT, leocrotta32,20, ghost46,20, Vlords64,18+63,19,
umberhulk62,20. STUN26342 curedPOax26343; keepOonforBaal. wROBE nowTHOROUGHLYBURNT+5 ACsame.
D35NEW AunknownPINK34,19 and EgainLEVEL40,20 BOTHBAGGED. Lightscroll57,20READ.
AMNESIAHAPAX60,18LEFT. MainmDEATH1:7 YPOLY1:6 eDIG0:2 rDIG1herouseS25,15.
D35routeUP12,19 W11,19 N11,17 E17,17 S17,19 E19,19 S19,21 E21,21 N21,17
E23,17 N23,13 E27,13 S27,15 W25,15 DUGS25,17 E27,17 S27,21 E29,21OPENdoor
E31,21 NE32,20 E34,20 SE35,21 E39,21OPENsecret E41,21 N41,20 E57,20
(FIRE49,20 avoidvia48,19..50,19; FIRE35,20avoid; SLEEP43,20benign)
N57,18 E63,18 S63,19OPENsecret S63,20 E70,20 S70,21 E71,21OPENsecret E73,21DOWN.
58,20WALL cannotdiglair. Mazeglyph▒CORRIDOR. Magict33,19 androck23,15.
OBS31:16:40healthy0drops. PublicnoteBaalfight. USERNO STOP KEEPPLAYING LIVE.

OLDER:
LATEST T26232 D35 hero12,19 UP, HP154 AC-20 XL17/665148 SATIATED. DescendedD34DOWN43,13!
D34 DOWN43,13 FOUND26231. D35UP12,19. eDIG(0:2) lastE40,17T26228.
mDEATH(1:7) YPOLY(1:6), allgearunchanged. OabouttoONtelecheck gOFF jEMPTY.
D34finalroute40,17 DUGEthrough41,17 to42,17 N42,13 E43,13DOWN.
D34hugefullreturntraildocumentedbelow; shortconnectionUP53,17toDOWN43,13probablyviaW53,14
butUNEXPLOREDwallsbetween43..51,14. CanlaterDIGtoshortenreturn. NoD34boss.
D35 entry░/▒around12,19 maybewater/doors? Needidentify. Warning1@11,21+20,21,4@17,27.
USER NO STOP KEEPPLAYING LIVE.

OLDER:
LATEST T26227 D34 hero40,17 HP154 AC-20 XL17/665148 SATIATED Ooff goff jempty.
AbouttoDIG E40,17 into42,17. BEFOREthiseDIG0:3 (lastE25,22T26197), mdeath1:7 Ypoly1:6 unchanged.
STORMGIANT14,20DEAD26156corpseLEFT +BOXUNLOCKEDsearched26166, onlyGREENgemleftinside.
NEWzCOLDunknown0herouses recoveredBOX14,20T26167. Gems4white/blue/redleftfloor14,20.
TROLL14,19DEAD26157 REVIVED~26176 nowroamingS16,22..23alive! Don'teatSATIATED.
VAMPIRE13,16DEAD26162 corpseLEFT. HUNGERring+145gold13,17LEFT. YELLOWpotionthrown26152
causedyawn (SLEEPINGlikely; bags2yellowstillunidentified). Nores/equipchanges.
ZRUTY23,22DEAD26187 corpseleft. MINOTAUR27,21DEAD26200 corpseleft, HPnadir141thenfull.
NewHORSEu28,23unknownpeaceful/hostile (warning1appearedsamepos), unengaged.
D34 ROUTE after10,13: E16,13 S16,20west12..13,16deadVAMPIREpocket;
DUGE16,20T26168through17,20, to18,20 N18,13 E25,13 S25,22.
W22,22 N22,16DEAD. DUGE25,22T26197through26,22 to27,22 N27,13 E31,13 S31,17
E40,17 N40,13 W33,13 S33,14DEAD. Return40,17currently.
BOULDER30,16bypassed31,16. TOP33..40,13pocketnoSTAIRS. DOWNstillunknown.
OBS30:33:05healthy0drops. PublicnoteD34Asmodeusdead/deathpolyreplenished. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T26145 D34 hero10,13 HP154 AC-20 XL17/663226 SATIATED Ooff goff jempty.
WUMPUS46,24dead26066 corpseLEFT. OGRELORD33,24dead26079 corpse+club+392goldLEFT.
HELLHOUND18,26dead26097 NOcorpse. GNOMEMUMMY18,25dead26098corpseleft.
SOLDIERANT3,23dead26112. Allotherspastunchanged; mdeath1:7 Ypoly1:6 eDIG0:5.
NearbySTORMGIANT12..13,18..20, VAMPIRE12..13,16..19, TROLL13..14,18..20 HOSTILEbehindwall11.
OtherMINOTAUR27,17 tele26118 unengaged. Wanderingz37,26ZRUTY likely, u32,20unknown.
D34 continuedroute from47,26magic: W46,26 N46,22 W39,22 S39,26 W33,26 N33,22
W30,22 S30,26 W3,26LONGcorridor N3,22 E7,22 N7,19 SE8,20 E10,20 N10,13.
BOULDER8,19 bypassSE8,20; BOULDER32,23 avoidvia33,22W30,22. RUST45,24avoidusing46,24.
NorthwestSPURS:10,13W6,13 S6,16 W3,16 N3,13DEAD, S3,20DEAD.
Currentlyback10,13 continueEunexplored, allfarNW branchesno stairs.
OBS30:13:46healthy0drops. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T26062 D34 hero47,26 HP154 AC-20 XL17/662417 SATIATED. Ooff goff jempty.
eDIG(0:5) lastW54,22T26048 openedwall53,22. mDEATH(1:7), YPOLY(1:6).
NEWrDIGunknowncharges fromBARROWWIGHT67,20 killed26028 recovered26029. NEWtTIN54,21picked26043.
RUSTTRAP52,22 hitHEAD alreadyMAXrusthelm, nochange. CUBE53,22DEAD26052 corpseLEFT.
MAGICTRAP47,26 T26057 summonedAIR ELEMENTAL killed26059, COCKATRICE48,25dead26060CORPSELEFT
andRAVEN46,25dead26061corpseleft. ax26062 curedblind/deaf; allHP154 after149low.
Nearbyq46,23 identifying. FarteleH39,17+14,19;T14,20;O39,24;V16,15;d25,22;
longWORM67,14tail69,13;z52,17;ant54,25. R/disenchalreadydead.
D34 exploredroute UP53,17 via54,16N54,14E57,14 S57,20 E61,20 N61,16 E70,16
S70,20 NW69,19 W68,19 SW67,20(lootpile) W64,20 S64,23 W60,23 S60,25
SW59,26 W54,26 N54,19deadend. From54,22 DUGWthrough53,22 to51,22
S51,26 W47,26(MAGIC). BOULDERS69,20 and60,26 bypassable. NEXTW46,26 N46,23.
OBS30:02:22healthy0drops. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T26010 D34 hero58,13 HP154 AC-20 XL17/661769 SATIATED. gOFF OOFF jEMPTY.
WREST SUCCESS4thattempt26008, wished2blessedCHARGINGp receivedboth, PwandDISINTEGRATED.
BothscrollsUSED26009/10: mDEATH(1:7), YPOLY(1:6) inventoryverified. OTHERemptyWISH1:0stillBOH,
mayWRESTanotherfinalwishinFUTURE. DoNOTrechargewishagain. Newwrest-wish guardWORKS.
NoCHARGINGscrollremaining. BaggedoldpEXTRAHEALunchanged.
DISENCHANTER transformed to BALUCHI Ypoly25990, killed55,14T25996 corpseLEFT.
mDEATH(0:1) afterTWOmisses25989/90; YPOLY(0:1). eDIG0:6.
Asmo loot dCOLD hFIRE MAIN unknowncharges. iSLIMEMOLD MAIN. Tfoodrationstillmain.
Retrieved P UNC WISH(1:0) fromBOH26006, attemptingWRESTlastwish, NOTrecharge.
OnefailedzP done. OTHERoldwish(1:0)stillBOH. Goalwish2BLESSEDCHARGING fordeath/poly.
Harnessnewwrest-wish command guarded20attempts; initialguardtooStrictcurrentlydebugging.
D34 UP53,17. DOWNunknown. MazeNdead58,13, explore57,14S57,15 next.
OBS29:54:41healthy0drops. USER NO STOP, KEEPPLAYING LIVE.

OLDER:
LATEST T25970 D34 hero52,18 HP149/154 AC-20 XL17/661394 SATIATED.
ASMODEUS DEAD52,18D34 T25970! LuredDOWNfromD33 whileadjacent25963, keptstandingD34UP53,17
toDENYdistantUPstairsHEAL, then ~12Excalhits. AsmousedoneEXTRAHEAL25966 thenDEAD.
NOconsumablesinbossfight, mdeathstill0:3, eDIG0:6. gLEVOFF OOFF jLAMP EMPTY. ALLfragilesBAGGED.
AsmodroppedFIRE/COLDwands52,18 unknowncharges(probablynearlyempty) PICKUPMENUab beingconfirmed.
D34 UP53,17. NearbyFOOD54,16unknown. Monsterwarning4@43,15. NoD34explorationyet.
D33 DOWN28,22 VERIFIED. INNERROUTE: eastHALL67,21W33,20 N33,19lockednowUNLOCKEDOPEN
N33,17 W30,17 secret29,17 OPEN W22,17 NW21,16 W20,16 SW19,17 AVOIDS PIT20,17;
door19,18OPEN S19,19 W17,19 S17,25 secret18,25OPEN E20,25 N20,21 secret21,21OPEN ->room22..30,19..23.
FIRE23,21 AVOID. ANTIMAGIC20,19. Scroll19,22 +26,21UNSEARCHED; POTION22,19UNSEARCHED;
Armor27/28,16 UNINSPECTED; leather24,17LEFT. Smallmimic27,16DEAD25890.
BONEDEVIL37,22 DEAD25872+2killerbeesdead25874; CREATEWAND37,22LEFT. MAGIC35,22;ANTI47,22.
D33 ASMOengaged25916 FledUP5,27 eachhit. Total~7hitsbeforeluredDOWN25963, dangeroussummons.
VAMPIRE LORD21,21DEAD25919 knifeleft. VAMPIRE22,20dead25925. Captain23,22DEAD25928
SILVERSABER+gearleft; captainSUMMONEDTROLL23,22DEAD25930 corpseLEFTcanREVIVE, DO NOT EATwhileSATIATED.
Horneddevil24,21DEAD25936 bullwhipleft. TwoERINYES28/29,21DEAD25947+25949,
summonedINVISIBLEHORNEDDEVIL27,23DEAD25950 tridentleft. No remaininginnerthreats excepttrollrevive.
AsmoNOnewcurses/equipmentdamage. SHOCKres25858 confirmed priorBLUEmeal.
RemainingD33 monsters x24..28,17 fromchugginghorned? farlooknotidentified; human71,23 outside;
barrowWIGHT+VAMPIRE escapedHOLE67,21 down toD34 beforeus aliveprobablysomewhereD34.
PublicoverlayD34AsmodeusDEAD. OBS29:42:34healthy0drops. USER NO STOP KEEPPLAYING LIVE.

OLDER:
LATEST T25861 D33 ASMODEUS hero55,21 HP154 AC-20 XL17/655429 SATIATED fromBLUEdragon.
SHOCK RESISTANCE ACQUIRED25858 "Your health currently feels amplified!" BLUEcorpse59,21ate25813.
LAMPj EMPTY wentout25765. gLEVOFF CfreeON Ooff. mDEATH(0:3) lastSE58,20killBLUE25779.
eDIG(0:6) lastE59,29T25720 shortcutto63,29. Otherresourcesunchanged.
Asmodeus INVS27,22 UNENGAGED, DOWN28,22 inINNERCHAMBER (maporigin15,15).
EASTHALL mainDOOR67,21 OPEN. HOLE67,21 CREATEDbybarrowwight25794 REQUIRELEV TOCROSS!
BARROWWIGHT withDIGwand escapedhole25794; VAMPIRE escapedhole25800 alivebelow.
NALFESHNEE57,20DEAD25776 butMASSsummoned blueDragon59,21 DEADm25779, leocrotta67,21dead25795,
centaur67,21dead25789, owlbear67,21dead25798, fireant67,21dead25796, dustVortex67,21dead25791,
ELFMUMMY61,21dead25781, orcSHAMAN66,20dead25802, LIZARD59,21dead25808leftcorpse,
SHOCKINGSPHERE exploded25807 noitemloss. BLUEcorpseEATEN25858 confirmedSHOCKres!
ICEDEVIL58,21dead25810 summonedSECONDice59,22DEAD25812. Noactivefoesnearhero.
MajorDEMON37,22 stillasleep identifying. Asmodeus27,22, horned25,20 stilluntouched.
MinHP122MIDANIMATION actual130lowest, nowFULL. Noarmor/curses/BUC lossfight.
D33 OUTERROUTE UP5,27 E15,27 S15,29 E17,29 N17,27 E19,27 S19,29 E21,29 N21,27
E25,27 S25,29 E33,29 N33,27 E35,27 S35,29 E53,29 N53,27 E55,27 S55,29 E59,29
DUG E63,29 N63,27 E65,27 S65,29 E69,29 N69,21 W67,21 DOOR HOLE thenWlonghall.
Deadends31,27(via25,27E),37,25(via37,27N),59,29beforedug. Westernspurs41,27/43,27/53,27Wunexplored.
TRAPS bear25,27 (legHEALED25597), WEB49,29, ROCK69,27, FIRE64,22+62,22monsrevealed (approx), HOLE67,21.
Tiger16,29dead25560 corpseLEFT. ROCKTROLL28,27dead25603ATE25606rottenblindcuredax25607.
TomGHOST25,27dead25620. VAMPIRELORD69,24dead25756. Nootheroutercombat.
PublicoverlayAsmoD33current. OBS29:17:27healthy0drops. USER NO STOP KEEPPLAYING LIVE.

OLDER:
LATEST T25534 D33 UP5,27 HP154 AC-20 XL17/651618. O BLINDFOLD ON, gOFF, jLAMPON.
D32 DOWN43,16 found25532 descended25533. HfoodrationFINISHED25376 nowT1mainfoodration.
D32 route24,13 E33,13 S33,16 W30,16 S30,19 E51,19 N51,16 E54,16 N54,13
W48,13 S48,16 W43,16DOWN. Deadend27,16via27,19. Newfire33,19 shieldfurtherburnt NOACchange.
POLY40,19 MRblocked. SPIKEDPIT55,13 AVOIDED. Jaguar53,13dead25500 bagunderCORPSEleft.
D33 probablyAsmodeus: telepathyhorneddevil25,20, major27,22 likelyAsmodeus (checking),
iceDEVIL7,17, demons37,22/56,22/57,20; human29,23; vampirebats24,22+34,18;
dog28,22 cat37,25 troll47,27 eye63,15. Noencountersyet. UP5,27 corridorE.
AllpotionsscrollsBAGGED inclpEXTRAHEAL, mdeath4,eDIG7,Gtele1,Xtele8,nstrike1,kstrike3herouses.
OBS28:51:51healthy0drops. PublicoverlayD32outdated. USER NO STOP KEEPPLAYING LIVE.

OLDER:
LATEST T25369 D32 hero24,13 goingE27,13. HP154 AC-20 XL17/651578 Dx18 Wi12 NOailments.
MASTER MINDFLAYER DEAD6,16 with mDEATH25156. ThenELFLORD8,13dead25162, RAVEN9,14dead25166,
ELFLORD9,17dead25171, OGRELORD6,13dead25179, BALUCHITHERIUM15,20dead25191, ETTIN16,25dead25210.
Allwesternspursdone:3,13deadend viaUP21,22 S21,25 W3,25 N3,13.
BLOCKAGE32,25 wasTWOBOULDERS32/33,25 notdeadend! kSTRIKE E25281 brokeBOTH.
MainkSTRIKE nowTHREEherouses total:24901N33,16,25281E31,25,25329W36,22.
ThenNEWBOULDER34,22 broken25329. mDEATH W34,22T25331 killedLURKER32,22 &DISENCHANTER29,22.
MAINmDEATH NOW(0:4). VROCK30,22dead25336. NOequipmentdrain,HPfull.
RoutefromUP21,22 S21,25 E45,25 N45,22 W24,22 N24,13 E(next)27,13 armoruninspected.
D32 FIRETRAP25,22 UNDER71gold noharm25338; FIRETRAP21,19; squeaky34,25.
BOULDER6,22 stillblocksautotravel evenmanualSE/NW bypass6,21<->7,22possible.
CorpsesleftMMF6,16,ogre6,13,raven9,14,elf6,21, green/baluchi15,20, ettin16,25,
LURKER32,22 &DISENCHANTER29,22 (DO NOT EAT), xorn14,22/owl13,22. JungleBOOTS9,17LEFT.
Gtele(0:1) Xtele(0:8) eDIG(0:7). nSTRIKE1charge. KslowCURSED0:1. Bcancel0:0NEVERbag.
ALLscroll/potionsBAGGED inclpEXTRAHEAL. yBLESSED GREASED54items. DOrb+FbellMAIN.
jLAMPON CfreeON gLEVoff Ooff. NoDOWND32yet. PublicoverlayD32AC-20current.
OBS28:33:57healthy0drops. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T25145 D32 hero15,21 OblindfoldON aftercheck ->nextRO2 planned. HP150 AC-20 XL17/648469.
BIG FIGHT D3215,22: nalfeshnee12,22 summon25126 masterMINDFLAYER14,22, greenDragon15,21,
xorn15,23/owlbear13,22/baluchitherium. Gtele1W25126 removedMMF, nowG(0:1).
THREE NALFESHNEES killed25129,25132,25135; XORNdead25134,OWLBEAR25138,GREENDRAGON25144.
GREENcorpse15,20LEFT; xorncorpse14,22/owlbear13,22, olderowlbear?11,22LEFT. Nofoodfromthese.
MMF ALIVE h6,16T25145, dangerous! Baluchitherium q12,14, ogrelord12,16, MINOTAURS3,19/72,19.
Elf-lords x6,20/21+9,18 andVampirebat9,14; VROCK25,22; Rrust?27,22; t32,22.
NalfCURSE25135: OrbRESISTED. OnlyKslowmonster nowCURSED(0:1). Fullinventorychecked,
ALL armorstatusfine apartfromfireerosion, yBOHstillBLESSED GREASED, DOrbBLESSED.
QGDSM nowverifiedBLESSED+1 (olderUNCincorrect), Cfree/glevBLESSED. BcancelUNC0:0MAINNEVERbag.
bNEWteleportscroll from14,22 recovered25137 thenBAGGED25138. BOH54items now.
EarlierMINOTAUR19,19dead25045 &ATEcorpse25046rottedblind1/7random thenfinished25055.
BatturnedVAMPIRELORD20,19dead25050, humanCORPSEleft. Horncuredblind25048.
D32FIRETRAP21,19T25061 burntROBEnowVERYBURNT+5 ->AC-20. Noitemsdestroyed.
D32 UP21,22. RouteUPW18,22 N18,19 E21,19 N21,13 W15,13 S15,22 mainfork.
Deadends18,16,12,19(via12,13south). Eastern31,25boulder32,25deadend. West21,25branchUNEXPLORED.
At15,22 Wcorridor9..15,22 newlyseen. East blankrock. NoDOWNfoundD32.
Gtele1left, Xtele8left. kSTRIKE1herouse, nSTRIKE1charge, eDIG7. Deathm6unusedsinceSurtur.
ALLscrolls/potionsbagged, pEXTRAHEALbagged, DOrb+FbellMAIN. jLAMPON. gLEVoff,CfreeON.
PublicoverlayD32AC-21OUTDATED updateAC-20. OBS28:11:54healthy0drops. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T25022 DESCENDED D32 UP21,22, HP154 AC-21 XL17/645108 Dx18 Wi12 noailments.
D31 DOWN75,15 confirmed! UP3,17. NewD32 CORRIDOR MAZE, warning3at24,21 +4at18,13.
D31 easternroutefrom59,29 E67,29 N67,27 W65,27 N65,25 E67,25 N67,23
E71,23 S71,25 E75,25 N75,23 E77,23 N77,21 W73,21 N73,19 W71,19 N71,15 E75,15DOWN.
Firetrap73,25T25003 burnt GLOVES nowUNC BURNT+2 ->AC-21, HP153thenfull. Noitemsdestroyed.
LEG HEALED25010 DX18. LeatherGOLEM73,22dead25011, leatherarmorLOOTLEFT.
All10recentstashes remainBAGGED seebelow, pextrahealingBAGGED notMAIN.
j lampON CfreeON gLEVoff Ooff. DOrb+FbellMAIN. BcancelNEVERbag. eDIG7remaining.
W0:0BAGGED; kSTRIKE1herouse33,16T24901. PublicoverlayD31AC-22OUTDATED updateD32AC-21.
USER NO STOP KEEP PLAYING LIVE.

OLDER:
LATEST T24987 D31 hero59,29 goingE. HP154 AC-22 XL17/644976 Wi12 Dx17.
FIRETRAP52,21T24935 scorched cSHIELD nowBLESSED BURNT+5 -> AC-22. Noitemsdestroyed.
ALLscrolls/potionsNOWBAGGED: oldrCURSEDVENZAR,oldLcreate,oldEtaming,oldAcyan,oldpBLESSEDEXTRAHEAL.
AlsoBAGGED oldtbrassring,oldzblessedtriangularamulet,oldUnewcircularamulet,
oldZ2UNKNOWNTINS found57,25,oldWEMPTYDIG(0:0) spentlastE49,23T24928 tunnelto53,23.
MainkSTRIKEused1N33,16T24901 boulderbroken33,15. Gargoyle32,13dead24905.
Firetrap49,22AVOID;firetrap52,21;teletrap54,23(WRENCH noactualtele); antimagic57,23.
Arrowtrap63,23; MINE61,27 exploded24964 nowPIT, woundedlegsDX18->17,
HPnadir147fromantimagicthenfull; BURDENclearedafterstash24967, hornnothing.
30searchrest24985 NOlegsbettermessageyet, ablewalkunburdened. Nootherailments.
BOULDERS new39,13,45,21,57,21 pushedcorner; MANUALDIAGONALBYPASS works.
Routefrom39,17 W33,17 N33,13 E38,13 SE39,14 S39,15 E43,15 S43,25 E45,25
N45,22 NE46,21 E47,21 S47,23 E49,23 DIGE51,23 S51,27 W49,27 S49,29
E55,29 N55,27 E57,27 N57,22 NE58,21 E61,21 S61,23 E63,23 S63,25
W61,25 S61,27 W59,27 S59,29 (currentbeforegoingE).
Deadendloop49,21->55,21S55,23 alltraploop. D31 stillNODOWN. Warnings5~49,19mindlessunID.
jLAMPON CfreeON Ooff gLEVoff. Orb/BellMAIN. BcancelNEVERBAG. eDIG7leftplusbagspares.
OBS27:51:41healthy0drops. OverlayAC-22updated. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T24896 D31 hero39,17 movingW; HP154 AC-23 XL17/644822 Wi12 noailments.
j lampON gLEVoff Ofoldoff CfreeON. DOrb/FbellMAIN. No consumables usedsince24715.
U NEWUNKNOWN CIRCULAR AMULET main picked13,23T24836 (NOT oldbaggedUmarker).
Captain19,23dead24794. Greenelf13,24dead24835. TwoBONEDEVILS25,23/22dead24861/63.
Fogcloud27,21wasVAMPIRELORD destroyed24869; whiteDRAGONSTATUE27,22wasGIANTMIMIC dead24872.
Currentroute from9,25 E11,25 S11,29 E15,29 N15,27 W13,27 N13,23 E17,23 S17,29
E21,29 N21,27 E25,27 N25,21 E27,21 S27,25 E29,25 S29,27 W27,27 S27,29
E37,29 N37,27 E39,27 N39,23 E41,23 N41,21 W39,21 N39,17 ->WEST unexplored.
Deadends15,25 and25,29. Boulder31,28 blocksbranchN butmaypush. Graystone32,29 LEFT.
Earlier westerncentral maze deadends15,19,13,21,19,27,25,19; boulders19,21/21,19
canmanualdiagonalbypass butAUTOTRAVELrefusesroutesaroundthem. Frontier13,13west,5,17north.
OBS27:36:49healthy0drops. NO DOWNFOUND. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T24731 D31 normal CORRIDOR MAZE hero15,17 headingN15,13. UP3,17.
HP154 AC-23 XL17/642846 Wi12. jlampON gLEVoff Ooff CfreeON. No ailments.
Wdig now(0:1), used1E at7,23T24715 toconnect7,23->11,23. eDIG0:7unused.
T new unknownBUCfoodration picked7,23. H1UNCfoodrationmain. New8ValleyitemsstillMAIN.
Twoelflordsdead11,22 +10,21 andGreenelf11,19 (LOOTleft inclgear/corpses).
Captainwarning4followingfromwest. Otherhuman15,26 unknown. BoneDEVIL25,22 viaPOconfirmed.
Anotherdemon25,23 unID; mimic25,17; g30,13; unicorn45,14; W70,21.
Route UP3,17->S3,21->E5,21->S5,23->W3,23->S3,25->E5,25->S5,27->E7,27
->N7,23->DIG E11,23->N11,21->W7,21->N7,19->E13,19->N13,17->E15,17.
Deadends northUP3,13east11,13+branch9,15; lower9,29west3,29north3,27.
No downstairsyet. PublicoverlayupdatedD31LV17HP154. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T24672 D30 DOWN4,12 CONFIRMED, accepted Gehennom enter y nextD31.
XL17/642381 HP154/154 AC-23 Wi12 RESTOREDax24636. jLAMPON, gLEVoff, CfreeON, Ooff.
ATE secondWRAITH21,19T24567->XL17 HP154. H now1foodration; mealPfinished24625.
IMPORTANT ERROR24632: Forceattackbatch killed giantzombieE, then PRIEST STEPPED IN and got hit.
MOLOCHPRIEST ANGRY ALIVE TEMPLE6,21vicinity. NO MORE forceattackbatches NEARPEACEFULS.
Reflection stoppedlightning butflashBLIND, axcured24636. HPnadir120 thenfullrecovered.
All8items altar RECOVERED24634, NO personalfloorcache. No prayer attempted.
Newmain: zBLESSED TRIANGULAR AMULET; tUNC BRASSRING; AUNC CYANPOTION;
rCURSED VENZARBORGAVVE scroll; LUNC CREATEMONSTERscroll; EUNC TAMINGscroll;
kUNC STRIKINGunknowncharges; vUNC SLEEPunknowncharges. All8stillMAIN NOTBAGGED.
nSTRIKING(0:1) used1charge24639 breakingtempleexit9,17. NO otherwand/potionuse.
Templeexit9,17brokenOPEN; secret11,15 &7,12 unlockedOPEN. Pit17,16 and8,13; sleepgas6,12.
Manyghosts/undead/deviIsremainValley, invisBONEDEVIL sleepwand SWgraveyard ALIVE, priesthostile.
Valleyroutemustnorthcross30..32,14 + southloop29,29->16,29->12,22->temple; variants2/3ON.
OBS27:12:02healthy0drops. USER NO STOP KEEPPLAYING.

OLDER:
LATEST T24542 D30 hero22,16 southernedgeNWgraveyard. XL16/322245 HP145/147 AC-23.
ATE FRESH WRAITH27,13at24499 -> XL16 HP147. jOILLAMP MAIN ON, gLEVoff, Ooff,CfreeON.
New main items kSTRIKING from59,20, rVENZARBORGAVVE from45,18, tBRASSRING63,16,
vSLEEPWAND from26,13. All unknownBUC/charges, zerohero uses.
Cleared many NWgraveyard wraiths/zombies/bats/vampirelord+vrock27,14.
VampireescapedE30+,14. RON/FRED/KARNOV/MAUD ghosts nearby, othersdead.
MIND FLAYER h59,21 distantbehind us. No combatwand or potion spent inValley.
Staticmap B letters are PASSABLE (not iron bars; older inference WRONG).
Mapvariant at raw27,12WALL -> actual30,23wall; northcross30..32,14OPEN.
Nextpath22,17->21,17->21,21->16,21->16,20->12,20->12,21->8,21TEMPLE.
Lots undead aheadesp21..25,17..19. Clearcarefully.
OBS26:57:59healthy0drops. USER NO STOP KEEP PLAYING LIVE.

OLDER:
LATEST T24385 D30 Valley hero70,26 HP140 AC-23, XL15/170080.
j OIL LAMP retrieved BOH and LIT24375; MAIN ON. O blindfoldOFF, g LEVOFF, C freeactionON.
Kenny ghost69,26dead24377; vampirelord70,25dead24383; another V73,25 formerlybat.
Zombie70,24 approaching, armor70,27uninspected; mummywrapping71,25.
Valley mapoffset CORRECTED x+3 y+11: UP69,28confirmed, DOWNlikely4,12, ALTAR6,21.
OBS26:42:25healthy0drops. Publicnote Valley. USER NO STOP KEEP PLAYING.

OLDER:
LATEST T24366 **ENTERED GEHENNOM D30 VALLEY OF DEAD** viaCastletrapdoor49,21 at24365.
Hero75,26; POtelepathyscanlotsundeadwestgraveyards. PendingRO44444 nextscreen.
HP140 AC-23 XL15/169185 STR18/21 Wi11, gLEVoff,CfreeactionON, OcurrentlyONuntilpendingRO.
S COLD(0:5) used1chargeD25giantEELeastfreeze24235. Jellyfishdead24237, babyYELLOWDdead24219.
XORNpetaliveD25island25,26last24258; leftsafe, no swaps. Palacehostilesunengaged, exteriorbypassed.
D26trolldead38,13at24287 corpseleft; CONFcuredax24287. D27/28clearroute.
CastleD29UP7,19 spears/daggers/EMPTYdigcache. Soldier9,20killed24336corpse/gearleft.
THRONECHEST46,21STILLUNSEARCHED. OGRELORD46,20dead24360corpseleft.
PEACEFULfiregiant42,20, 2goldennagaswesthall. 7soldiersapproachingrearfromthroneroom.
REARSECRETDOOR47,21found24358 thenkeyUNLOCKandOPEN24364. Step49,21gOFF→Valley.
SleepingDRAGONS56,18/19/23/24notdisturbed, don'twakeunnecessarily.
ValleyMAPsource https://raw.githubusercontent.com/NetHack/NetHack/NetHack-3.6.7_Released/dat/gehennom.des
ValleyNOteleport/NOdig/NOmapping. Staticmaplikelyoffsetx+2,y+11. DOWN3,12, BRANCHUP68,28,
MOLOCHALTAR5,21 priest7,21peacefulunknownuntilfarlook. LotsW/bats/ghostsgraveyards.
NoPRAYERinGehennom. Lastprayer24120safeTyrwellpleased; noanger. PermanentSEEINVIS24122.
Nochargedwishesleft k/P1:0BAGGED; Umarker1:11BAGGED nofurtherrechargeanyofthese.
OBS26:32:29healthy(~3minago). USERNOstop KEEPPLAYINGLIVE.

OLDER:
LATEST T24123 D19hero19,12 returningDOWN54,16. **PERMANENT SEEINVISIBLE acquired24122**
blesseddSEEINVIS viaiwaterdip thenquaff. d/i gone. HOLYWATER1stillDIRECTyspare.
**PRAYER SUCCESS24120**, made1holywaterthenconsumedblessingseeinvis. Tyrwellpleased,
anger0, cooldownRESET24120 nofurtherpraysoon. Mimicoffer24116CLOVER provespreviouscooldown0,
addedluck(~2). MIMIC19,12DEAD24112 andcorpseoffered, nootherfloorcachechanges.
HP140 AC-23 XL15/167152 Wi11. pBLESSEDEXTRAHEALINGmain,H2FOODRATIONSmain(lastmeal24037).
AllarmorON,gLEVoff,CfreeactionON,OblindfoldOFF. Umarker1:11+emptyk/PwishBAGGEDdirecty.
Bcancel0:0MAIN neverbag; DOrbMAIN. Nootherresourceuses. OBS26:17:06healthy.
NewD14pit23,20, peacefulTENGU/ALEAXleftnearaltar, allbelongingsrecoverednofloorcache.
USERNOstop CONTINUEPLAYINGLIVE.

OLDER:
LATEST T23954 D14ALTAR24,17 **AC-23 FULLARMOR RESTORED**, HP140,XL15/166969,Wi11.
ARMOR: cBLESSED+5shield, wBLESSED+5BURNTrobe, sBLESSEDfireproof+3SPEED,
NBLESSED+4THOROUGHLYRUSTYhelm, QBLESSED+1GDSM,uUNC+2gloves,MUNC+0shirt,IREFLECTION.
P finalwish23941 requested3blessedEA got1v, read23941shield3->5. **BOTHk/P(1:0)EMPTY, NEVERrecharge**.
U BLESSEDMAGICMARKER now(1:11), rechargedONCE23948 NEVERagain. ALL8blanksUSED,
charging+identify+6EA. EA formallyknownYUMYUM. Remainingmarker11goodknowncheapscroll butneedblank.
**TYRANGER0 AGAIN23940 viaSTALKEROFFER** 'mollified'; luckreset0. PRAYERCOOLDOWNACTIVE,
lastwish23941 adds50..149, don'tprayuntilsacrificereconciliationorlonginterval>500.
J CREATE0:3 currently; used6charges Aleax/freezingsphere/housecat/manes/stalker/tengu.
PEACEFUL ALEAX25,18 andTENGU24,18 nearby NEVERATTACK. Anotherstalkerfar64,16unengaged.
NOLOOTFLOOR: waterpicked i23954 andnowBAGGING pending, U/k/P alsobaggingpending.
MainH3foodrations,o/qLIZARDS; emergencyblessedEXTRAHEALING andHOLYWATERdirecty.
Plan retrieveextrahealing, descendtowardGehennom. ORBinvokeUNCONTROLLEDwithouttelecontrol don'tuse.
gLEVoff CfreeactionONright OblindfoldOFF. OBS26:06:59healthy, publicnoteupdateneededAC23.
USERNOstop KEEPPLAYINGLIVE. Followingolderstate superseded.

OLDER:
LATEST T23926 D14 ALTAR24,17. PREPARATION ongoing, water1UNC onfloor only. Alloldfloorrepacked.
CRITICAL PRAYER MISTAKE23916: markerWISH23904 ADDS50..149PRAYERCOOLDOWN (zap.c5098).
Prayedtooearly -> TYRANGER1, luck-3, Wisdom12->11. Excaldrainres preventedXLloss.
NeverpraysoonafterWISH! Needcorpsedifficulty>=8 tosatisfyanger, then cooldownreconciliation.
Housecatoffer23925 'inadequacy' noangerreduction. Jcreate9->5charges (Aleax, sphere,cat,manes),
pendingF4F3F3zJ NEXT screen. PEACEFUL ALEAX near27,17 NEVERATTACK. 2manes stillat23,17/25,18.
U BLESSED MAGICMARKER wishedk23904 unknowncharges. k(1:0), P(1:1) ONEchargedwishleft NEVERrecharge.
8UNC BLANKSCROLLS madeBcancel23912 NOWDIRECTy (oldh). Bcancel(0:0)neverbag.
jHOLYWATER,dUNCSEEINVIS,pBLESSEDEXTRAHEALING allDIRECTy currently. L oilskinsackDIRECTy now21items,
removedamnesia1/create5/light2→8blanks andblessedblindness→waterfloor. Otherunknownscrollsintact.
IDENTIFYbBLESSED read23882 FULLMAIN ID: H oilLAMP (bagged), tLOCKING0:3(bagged), iSTINKCLOUD(bagged),
d SEEINVIS(bagged), hMONSTERDETECT(bagged). SIXringsbagged: clay+2ADORN, coralSTEALTHcursed,
emerald-2STRcursed, shinySHAPECHANGERPROTECTION, tigereyeHUNGERcursed, wireWARNING.
WandsKNOWN afterID: eDIG0:7,mDEATH0:6,nSTRIKE0:2,GTELE0:2,Kslow0:1,Rfire0:1,
Scold0:6,Vmm0:2,Wdig0:2,Xtele0:8,Ypoly0:2. Fbell0:3,DOrb0:5 MAIN.
Currentfood H3rationsMAIN,o/qLIZARDSmain. ALLotherfoodbagged. s+0fireproofspeed BLESSED,
u+2glovesUNC,w+0burntrobeUNC,N+1thoroughrusthelmBLESSED,Q+0GDSM BLESSED,IreflectionUNC.
SCAREMONSTER PRATYAVAYAH LOSTcrumble23890afterrepick. Nootherloss. Allgems/gold/repacked.
HP140/140 AC-9 XL15/166814 gOFF CfreeactionON. OBS25:56:01healthy. USERNOstopCONTINUE.

OLDER:
LATEST T23880 D14 TYR ALTAR24,17: inventory sorting IN PROGRESS, MANY VALUABLES ON FLOOR.
y BOH emptied #tip23873, then12spares stashed23880 (food4C/ration/cookies/jelly, pEMPTYstriking,
jnewDIG,rSurturTELE,zoldCREATE,vOPENING,Zluckstone,Uwhistle). Bcancel NEVERbag; DOrbMAIN.
Floor: oilskinsack28items, 1280gold, waterboots, food/tripe, scare+curseTELEscroll,
murky+HOLYWATER+cursedheal/extraheal, sixunknownrings,+1accuracy,DIG,LIGHT,SLOW,leash,gems.
Some pickups INPROGRESS: inspect next screen. bBLESSEDID and iBLESSEDELBIB scroll MAIN,
dUNC BRILLIANTBLUE potion MAIN, HunknownLAMP MAIN. NeedIDlamp andunknowns, REPACKfloor beforeleave.
HP140/140 AC-9 XL15/166770 STR18/21 gOFF CfreeactionON OblindfoldOFF. Warning2 near29,20.
OBS25:39:23healthy0drops. NO USER STOP; continueplayinglive. Followingolderqueststate superseded.

OLDER:
LATEST T23804 HOME1 SHRINE hero36/37,20, **QUEST COMPLETED BY NORN23804**. OrbentrustedforAmuletquest.
**D ORB OF FATE** + **F BELL OF OPENING MAINPACK**, DON'TbagORB (halfdamagewhilecarried).
HP140/140 AC-9 XL15/166769 STR18/21. gLEV ONleft CfreeactionONright OblindfoldOFF. Noailments.
New**S WAND OF COLD** fromHOME5giant29,18killed23704, **0herouses,2monsteruses**, unknownBUC/remaining.
**L NEWFORTUNECOOKIE** samegiant. OldLwaterbootsBAGGEDdirecty. ColdwandSNOToldwirering(thatbagged).
Home5DOWN30,19 UP21,19; nearstairsGIANTdead23704 antsnearcleared, 2giantsfarEremain+newantsSW.
Home4DOWN7,18 UP35,18 straight28eastlevreturn; killed1ant23721, giants32,16/17+41,20left.
Home3DOWN41,21 UP69,29 returnrouteWESTto21,21 then7to20,20 then1to19,21 thenS19,29 thenE69,29.
**Arrowtrap31,21** newlyfound23733; firetraps38,25+40,24existing. Boulders20,21+20,22 bypassNW.
GIANTBEETLE28,29 killed23757 corpseleft; FIREANT50,29 killed23771 corpseleft, newh51,13farunengaged.
Home2DOWN53,30 UP43,20 nearantkilled23789, mapmostlyice noactiveknownenemies.
Home1DOWN21,12 PORTAL69,28 exitsD1119,14. NeedleaveEdoor46,21 blockedbyboulder44,21 inside,
canwalknortharoundboulder44,20→45,20 then45,21→46,21eastdoor intactnodiagonal.
NORN38,21peaceful, guardiansallpeaceful7left, chest39,21unsearched. Don'tattackNPCs.
Plan exitportal then D14/15altar forBUC/identify/holywater/improveAC beforeGehennom.
**mDEATH1use, Kslow4uses, Vmagicmissile2uses, Gtele3uses, pEMPTY, nstriking3uses**, restseeprior.
**k WISH1:1 P1:1 TWOchargedwishes**, NEVERrecharge. yBLESSEDBOH, BcancelNEVERbag.
**Fholywater+IDENTIFYscroll areBAGGEDdirecty**, lettersreusedORB/BELL. Lotsunknownpotions/ringsbagged.
**H unknownLAMP MAINPACK** couldoil/magic, notyetID. All3foodrationsDIRECTy. HungerNOTyet.
OBS25:17:23healthy(~4minold). PublicnotequestCOMPLETEpreparingGehennom. USERNOstop KEEPPLAYING NOFINAL.

OLDER:
LATEST T23698 HOME5 hero30,19 DOWNSTAIRS returning, Pg_@<pendingto21,19UP.
**LORD SURTUR DEAD23678**, **D ORB OF FATE MAINPACK** + **F BELL OF OPENING MAINPACK** recovered23680.
**m BLESSED WANDOFDEATH** wishedk23677, **1USE killedSurtur23678**, remainingunknown4..7.
**k WISH(1:1) P(1:1) TWOchargedwishesleft NEVERRECHARGE either.**
**K SLOW4uses total**, slowedSurtur23653, Ypoly6 Rfire7 unchanged. Vmagicmissile2uses total(engrave+zap23649).
**p STRIKING EMPTY confirmed23651** 2herouses+monsteruses exhausted, mainpack. noldSTRIKING3uses unchanged:
attempt8zn2gotFLUSHEDbySurturarrival23652, NOzapmessage, bridgeNOTDESTROYED! BothdrawbridgesINTACT.
**G TELEPORT3uses** selfescapeLAVA23685. Xtele0, **rNEW TELEPORTfromSURTUR0herouses** unknownremaining.
**jNEW DIGGING0uses** fromHOME6floor51,16 MAINPACK (differentfrombaggedjHome3).
HP131/140 AC-9 XL15/166353 STR18/21, gOFFuntilpendingPg, CfreeactionON, OblindfoldOFF.
**D/F no longerIDscroll/HOLYWATER: theseareBAGGEDdirecty, lettersREUSEDORB/BELL. DO NOTbagORB.**
Home6 UP68,23. **67,22 isLAVA**: misreadwalkedinto23682gOFF, gotstuck; PglevalonedoesNOTimmediatelyfree,
needsstruggleturns. BadPg3Rg<batchturnedlevOFFagainwhileSTUCK. **zG. TELEPORTEDOUT23685saved**, NOdeath.
ThenPg restored andautotravelUP68,23, verifiedbeforeRg<23698. NOitemlossreported, ACunchanged.
ALWAYS PgBEFOREmovingafterlanding, neverassumefloorbyvisualspacing. UseMapfeaturesfor'}'.
SurturcorpseLEFT67,21 (floor), deathweaponnotloot. Orb+BELL+rteleallsecured. Northguards7killed,
~4giantsremainincludingoneDEATHWAND('curved') giant TELEPORTEDunknownposition. MR+reflectionbothON.
Home6 NORTHBRIDGE40,15 +GATE40,16 INTACT, SOUTH40,27+GATE40,26 INTACT. No needreturn.
Home6 northboulderloot44/45/47,13 unsearched, magicmissile/fire/deathwandspossible, notworthnow.
NoSurturresurrection. NeedreturnNORN38,21HOME1 withOrb tocompletequest.
Publicnote updatedSurturdeadartifactrecoveredreturning. OBS25:04:41healthy~5minold.
USERNOstop CONTINUEPLAYINGLIVE NOFINAL.

OLDER:
LATEST T23593 HOME5 hero30,19 DOWNSTAIRS; F4F4Rg>pending(afterantkill messageanimation), readscreen.
HP140/140 XL15/164097 STR18/21 **AC-9 robeSMOULDERINGfiretrap23537**, otherarmorok, sSPEEDfireproofconfirmed.
gLEV ONuntilpendingRg thenDESCEND toHOME6goal. C FREEACTION ONright. NO USERSTOP KEEPPLAYING.
HOME4 UP35,18 DOWN7,18, straight28WESTlevcrosslava. Entiremaplavaoutsidepaths. HostilesEhalfLEFT.
HOME5 UP21,19 DOWN30,19, ant29,19killed23593; giant28,17approaching fromNfiretrap.
HOME3 UP69,29 DOWN41,21. ALLinitialgiantsdead(7fire+2stone),~18fireantskilled. Noactiveknownhostiles.
Home3LOOT22,21 gems/corpsesremain; pickedD IDscroll, V TINMAGICMISSILE1engraveuse23514,
jNEW DIG0uses thenBAGGEDdirecty. mNEWSLOWMONSTER0usesalsoBAGGEDdirecty.
**K SLOWMONSTER2uses, pNEWSTRIKING2uses**. k1:2 P1:1 NEVERrecharge.
**H NOWLAMP** unknownoil/magicBUC picked32,20Home3. All3HfoodrationsDIRECTy beforehand.
**L WATERWALKINGBOOTS BAGGEDdirecty**; letterLreusedEIRISSAZUNIDISI scroll thenBURNED23537, NONEleft.
Mainpackfreedb/i/S/r/j/m/d: all**clay/shiny/wire/+1acc rings, sparejDIG,mSLOW,dLIGHT, Lwaterboots DIRECTy**.
**D IDENTIFYscroll DIRECTy, F HOLYWATER DIRECTy**, preservedfromfiretrap.
Home3picked**bBRILLIANTBLUEpotion41,25 DIRECTy**, **SLEASH36,25 DIRECTy**.
**d SCAREMONSTER(PRATYAVAYAH) from52,25 DIRECTy**, successfullypickedonce unknownBUCcouldcrumbleifdrop+repick.
**i ELBIBYLOH unknownscroll from57,23 DIRECTy**. Newscrolltypesnotread. EIRISburnednolongerowned.
Home3 FIRETRAPS38,25(triggeredrobe+Lscrollburn), 40,24(searched). ALLnewlootsbaggedexceptVwand+Hlamp.
Cloudygiantdrink23576? actually23476 'looks much better' likelyEXTRAHEALING, have2baggedvariants.
OBS24:56:53healthy0drops (~3minold). NeedreadNEXTscreen confirmsHOME6 beforeactions.

OLDER:
LATEST T23505 HOME3 hero21,21 atWEST narrowentrance, HP140/140 AC-10 XL15/163957 STR18/21.
**C FREE ACTION ring ONright** wishedk23407 thenPC23408. **k1:2 P1:1, THREEchargedwishesleft** NEVERrecharge.
**gLEV ONleft**; nowonlyonefingerfree whenputtingg usePg (NOTPgl, lbecomesloot). OblindfoldOFF.
**a+3EXCALCONFIRMED** inventorypanel. FIRE/COLD/POISON/SLEEP/DISINTEGRATION/MR/reflection/freeaction.
Kslow2uses total (second23469 slowedgiant+ant). pnewSTRIKING1use23487, **SECONDusepending23506**.
Home3UP69,29, DOWN41,21. Westentrance21,21safeoneenemyfunnel. BOULDERS20,21+20,22,22,21.
22,21bouldertobreakpsecondzap6pending. ~7FIREGIANTS+2STONEGIANTSkilled here manyfireants; fewantsbehindboulderstill.
GIANTLOOT22,21: tinwandunknown, foodration, manygems/corpses; loot23,21/23,20 too.
Home3unsearchedscroll30?,18 /56?,23 /51?,25, wand27?,24, tools32?,20+35?,25, potion40?,25.
Darkgreenpot=PARALYSIS (giantthrewHome2T23400). CLOUDYpotgiantdrank23476 'looks much better' likelyEXTRAHEALING.
Havecloudyblessednestedoilskin+unknownDIRECTy; notyetcalled/verified. Noailments, NOTSATIATEDnow.
Home2UP43,20 DOWN53,30. Firegiantkilled49,28T23405corpseleftnowold; fewunsearcheditems.
Home1DOWN21,12 portal69,28 NORN38,21 QUESTACCEPTED23371. OneWARRIORambientfiretrapdrowned23385,
NOTHEROfault; noattackonpeaceful. Westdoor29,21brokenpassable diagonal. Questcontinue.
OBS24:49:24healthy0drops, USERNOstop KEEPPLAYINGLIVE NOFINAL.

OLDER:
LATEST T23373 HOME1: NORN ACCEPTED QUEST23371, hero39,20, gLEV ONleft again23373.
HP140/140 AC-10 XL15/161175 STR18/21, SATIATED fromFIRSTgiantmeal23341..23364. DO NOTeat.
Bothgiantcorpses eaten, allgems DIRECTy. CURSEDringsm/j alsoDIRECTy. pnewSTRIKINGmain.
Boulder44,21 now, eastdoor46,21OPEN, west29,21OPEN. Norn38,21peaceful, chest39,21unsearched.
NeedleaveWEST then HOME DOWN21,12 (sourcecoord18,1 +3,+11). LevOFFonlyONSTAIRS.
Fire resistance YES23336. TyrANGER0. kWISH1:3 P1:1 NEVERRECHARGE. Fholywaterunused.

OLDER:
LATEST T23337 HOME1 HERO47,23 ON ICE **gLEV RING OFF** (removed23331 to eat) MUSTONbeforelava.
**FIRE RESISTANCE GAINED23336 firegiantcorpse: 'You feel a momentary chill.'** Rottenfoodrandomquarteredmeal
completedquickly5turns; noillness, NO STRgain. HP140/140 XL15/161175 AC-10 Wi12. NOTSATIATED.
**p NEW STRIKING WAND** fromfiregiant, 0heroUSES monsterused2times, unknownBUC/remaining.
**C3BLACK D3BLUE V3GREEN GEMS** picked23337; nextaysCaysDaysV bagsDIRECTy then','pick4WHITEleft47,23.
GemsletterCwilllikelyreusedwhite, check. **p IS NO LONGER CHARGING** thatscrollconsumed22852.
Killed~10fireants (onecorpse63,27ate23303 NOres), 2FIREGIANTS:
FIRSTfiregiant46,21 doorway killed23317 leftBOULDER46,21+maybeCORPSE UNDERNEATH unsearched.
SECONDfiregiant47,23 killed23325, corpseEATEN23336 nowwand+gemslooted. Nootheradjacentmonsters.
**EAST SHRINE DOOR46,21 unlockedlkey23315 THENopenedbyfirstgiant, NOWBOULDERBLOCKS.**
Needfromhero47,23 go88to47,21 then4PUSHboulderwest45,21 whilegOFF (can'tpushlev), checkfriendlyNPCblocked.
Shrineinterior30..45,19..23, **NORN~38,21**, 8peacefulWARRIORSroam. **DO NOT RANGED ZAPTHROUGHSHRINE**.
Nornnotspokenyet. Westdoor29,21open, firegiantsroamedthroughbuildingfromW.
Homeportal69,28 backD11portal19,14. KeepgLEVONquestexceptcheckedfloor/iceforpickup/eating/pushing/stairs.
Home lava region50..53,17..21 and55/56,18..21; ***56,21 LAVA*** (crossedlevsafe).
OtherLAVA/poolmany, cannotdistinguishtext'}' needfarlookiflanding. Hero47,23verifiedICEsearched10no trap.
**k WISH1:3 andP1:1, neitherrechargeagain**. F HOLYWATER untouched. OBLINDFOLDOFF Kslow1use.
OBS24:14:58 lasthealthy(~8minold), NO USERSTOP KEEPPLAYINGLIVE.

OLDER:
LATEST T23287 D11 **QUESTPORTAL19,14 FOUND** inNWsmallroom. InitiallyenteredHOME1T23286.
**HOME1 ENTRYPORTAL69,28**, Pg l onportal activatedportalAGAINreturnD11! gLEVONNOWleftfinger.
Nextcommand64 stepEoffD11portal thenWback toQUEST. **STEP OFF HOMEPORTAL BEFORE LEV CHANGES.**
HomeShrineofDestinyterrainLAVA/WATER, gLEVONMANDATORY, sSPEEDBOOTS ON. Nornnotmetyet.
HeroXL15/160443 HP140/140 AC-10 Wi12 noailments. Questfireants65,28,61,25,etc; wantFIRErescorpseeating.
**OBS24:14:58 active0drops/reconnect/congestion. NO USERSTOP, CONTINUEPLAYING.**
D11 discoveredsecretDOOR49,23fromUProom (notneededportal), ant58,19 outsideexploredmapunknownroom.
D11HOBBIT38,25 confirmednotmindflayer, giantspider6,19farwest, GREENMOLD41,14downroomleft.
SearchedcentralSroom+NEroom noportal, unnecessaryD11stairsroomsearch(ignore).
D14 COCKATRICE22,18 killed23001 noSTONE/corpse; RAVEN32,22 killed23008 blindcuredhorn23009.
D13 cockatriceDISAPPEAREDduringtravel23027 aliveunknown. D12violetfungus51,16 hitnotkilled23030 bypassed.
D16 killsGREENMOLD57,16,3APES66/65/52,13/14,GNOMEZOMBIE54,13,TROLL47,13nocorpse,PLAINSCENTAUR9,20.
AllwandsunchangedexceptKslow1use; k1:3 P1:1 NEVERRECHARGEeitheragain. pCHARGINGnoneleft.
gBLESSEDLEV ring onLEFT, OBLINDFOLDOFF; Fholywateunused mainpack; q/oLIZARDSmainpack.

OLDER:
LATEST T22853+ D19 ALTAR17,12 HP139/140 AC-10 XL15/160000. ALLARMORON inclM+0shirt.
**C CURSEDGENOCIDE CONSUMED22826 reversegenocideWRAITHS sixsummoned/allkilled22837.**
THREEfreshwraithcorpseseaten22838/39/41 -> XL12->15, maxHP140. NOleveldrainExcalprotects.
**V BLESSED IDENTIFY scroll found17,13 andread22850 -> kWISH(0:1), rBLESSED+1INCREASEACCURACY(opal).**
**k LASTcharge USED22851 wishBLESSED RING OF LEVITATION -> gSILVER**; dropaltarconfirmedblessed.
**p BLESSED CHARGING CONSUMED22852 rechargedk ONCE -> k(1:3). NEVER RECHARGE k AGAIN.**
**P WISH(1:1) unchanged ALSO NEVER RECHARGEAGAIN. TOTAL4chargedwishesleft.**
gLEVRING actionPglRg pendingtestthenremove; shouldOFFafter; OBLINDFOLDOFF, Kslowwand.
**K PLATINUM wand calledSLOWMONSTER, engravingtest22844 'bugs slow down', 1chargeused.**
**ENGRAVEONALTAR MISTAKE22842 -> Wisdom-1 andalignmentrecord-1, NOnewdivineanger.**
WisdomRESTORED12 withhorn22846. TYRANGERREMAINS0 fromnagaoffering22798. **NEVERENGRAVEONALTAR.**
H NEWFOODRATION pickedALTAR22842. ExcalHenchscrollconsumed22810 expected+3(confirminventory).
g OLD CURSEDHEALING is INSIDEy(notmainpack; lettergREUSEDforLEVring). Dcursecoralbaggedtoo.
F HOLYWATERmainpack stillunused. Oldoilskin INSIDEy28items; letterVwillreassignsinceVscrollconsumed.
Mapnearaltar: LARGE MIMIC19,12 stoneunengaged; peacefuldwarves19/21,12 diggingNwall17/18,11.
VERR YED HORRE unknownscrollfloor16,12 witholdORANGEDRAGONcorpse/scales; worthpickupBUCthenbag.
WoodlandELF killed17,14T22825 corpse+lootleft, JAGUARoldcorpse18,14leftDONOTEATnowold.
**NO FIREres** still, questfireants/giants canconvey. NeedlevONquestlava, noDRAWBRIDGESTANDING.
OBS23:53:38active0drops/reconnect/congestion. NO USERSTOP, KEEP PLAYINGLIVE.

OLDER:
LATEST T22824+ D19 ALTAR17,12 HP119/119 XL12/36264. ARMOR: M UNC+0 HAWAIIANSHIRT WORN22819;
Q GDSM backON22824; Ww commandpendingrestoresrobeAC-10. sSPEEDBOOTS ON, LwaterOFF.
**TYR ANGER RESOLVED T22798: rednaga sacrifice -> 'Tyr seems mollified.'** No prayer usedyet.
J CREATE MONSTER now3uses (third22783rednaga); Ypoly6,Rfire7,Wdig2,Bcancel1left unchanged.
Rednaga corpse2600 liftneededDROP mostloosegear&bag thenovertaxedcarry1step. OfferingdoneallgearRECOVERED.
**C CURSED GENOCIDE mainpack**, removednestedbag. **F BLESSED WATER (HOLY) mainpack** alreadyblessed!
PlanKEEPcursedgenocide forreversegenocideWRAITHS toreachXL14quest; NOTreadconfused.
**O NOWBLINDFOLD (OFF); K NEW PLATINUM WAND unknownBUC/type0used**, foundONaltar aftermonsterloot.
Alloldlettersotherwise same (Jcreate,kcastle,Pwish1:1 etc). Oldoilskinsackformerlyo nowVbutINSIDEyagain28items.
**g HEALING CURSED +D CORALRING CURSED -> bothbaggedDIRECTy22811**; nohealingpotionmainpacknow.
**H UNC ENCHANTWEAPON consumed22810**, Excal+2->expected+3(verifyinventory).
**y BOH CONFIRMED BLESSED** altar22803. VcockatricecorpseROTTEDinsidey (notinbaglist).
**Fwater +Ccursedgenocide** retrievedfromoilskinsackwhichnow28items. Fnotusedyetnoholywaterduplication.
**m LARGE MIMIC19,12 disguisedstone**, stationaryunengaged. Peacefuldwarves17,11(digging)/23,12.
Woodlandelf18,15 woundedapproachinglast22824, leprechaun~40,15 fled (notkilled).
DWARFMUMMY killed22788(noownracecorpse); lastHOMUNCULUS killed22800; rednaga22784offered.
Hero82goldmainpack frommummy, 4800bagged. Wholeo/partialqLIZARDS stillmainpack.
OBS23:41:08active0drops/reconnect/congestion, NO USERSTOP CONTINUE PLAYING LIVE.

OLDER:
LATEST T22782 D19 TYR ALTAR17,12, HP107/119 AC-10 XL12/36045. KOFF. s SPEEDBOOTS WORN again22669; L waterboots OFF.
Returned safely fromCastle; XORN LEFT ALIVE D25 centralisland last23,24T22644, couldnotcrosswater.
Ofoodration consumedD24T22665. o WHOLELIZARD mainpack; oldoilskinsack INSIDEy (letterwillreassign).
C2tripe+Funknowncloudy baggedDIRECTy22567/68. g unknownHEALING mainpack.
**TYR ANGER1 STILL; NO ATONEMENT YET, PRAYER UNSAFE.** D19 altarverified17,12.
J CREATE MONSTER used2times22760/22768; nextcommand6zJ thirdpending.
Y POLYMORPH6uses (fireelemental->ORANGEDRAGON22761). R FIRE7uses, Wdig2, Bcancel1left.
ORANGE DRAGON killed22764 at16,12 corpseTOOHEAVY4500 cannotlift/kick, leftwithscales.
H ENCHANTWEAPON scroll collectedfromdragon, unknownBUC mainpack. Noextra wishesused.
SecondJ spawnedcrowd; HILLGIANT killed22771 at19,13 leftBOULDER noobviouscorpse.
Fireant killed22771 ONALTAR17,12, ate22782 NOFIREresgain. Homunculus,werejackal,jaguar,Qmechanic killed.
Jaguarcorpse18,14 (T22775) left. Q no corpse. WoodlandELF woundedfleeingS18,18;
leprechaun18,13 alive; PEACEFUL TENGU andDWARF nearby DO NOT ATTACK.
Pwish(1:1) NEVERRECHARGE; kCastle0..2remainingunknown, pblessedCHARGING1 reservedfork.
OBS23:32:35 active0drops/congestion/reconnect. NO USERSTOP, KEEP PLAYING.

OLDER:
LATEST T22566+ D25 MEDUSA hero7,22->SE8,23 next, HP119/119 AC-10 XL12/34944 KOFF NOTSATIATED.
**L WATERWALKING BOOTS WORN since22484, sSPEEDBOOTS OFFpack.** Slow now normal/intrinsicuncertain.
**o NEW WHOLE LIZARDCORPSE MAINPACK** fromD28 42,19T22240; oldqPARTLYEATENlizardstillpack.
WARNING oletterREUSED; oldOILSKINSACK is INSIDEyandletterwillreassignwhenremoved.
**R FIRE NOW7USES** twozapsD28cockatrice/lizard22238; remainingUNKNOWN0..1likely, preserveforemergency.
**W DIGGING NOW2uses** second22237 dugD28wall42,19 shortcutDOWN43,19->W41,19(returnpath).
Ypoly5uses,Bcancel1LEFT,Pwish(1:1),kCastle0..2unknown1usednevercharged,pcharging1 unchanged.
**PET TAME INVISIBLEXORN successfullyfollowedD28,D27,D26,D25**, lastD257,18nearMedusastatue,
fought+killedPEACEFULBLACKNAGA6,19T22561; noheroattack/guilt. WilllikelyremainONcentralisland
whenwewaterwalk. DO NOT PETSWAPFROMWATER. Userinformedmayneedleavepetsafelyhere.
D28cockatrice38,19 killedfire22238 corpseLEFT; LIZARD42,19 killedsamebeamcollectedo.
GRAYOOZE9,13 killed22269globate22272 acid7HP **NO FIRE RESGAINED**; snake7,20killed22297.
D27 ettinMUMMY26,15 destroyed22434 corpseLEFT(oldDONOTEAT); peacefulsasquatchleftalive.
D26 shapeshifterat26,13 babyYELLOWDRAGON->GLASSGOLEM killed22519, gemsleft26,13.
D25 BABYYELLOWDRAGON7,22 killed22564 corpseleft7,22. **C2TRIPERATIONS +F CLOUDYPOTION**
picked22566, currentlycommandaysFaysCbaggingDIRECTy. OLD blessedcloudyinsideoalsoexists.
OurcurrentnextpathSE8,23 ->9,24WATER ->10,25WATER ->E15,25LAND ->E23,25 ->24,26LAND
->26,28WATER ->28,28WATER ->32,28WATER ->38/39,28LAND ->40,28LAND ->46,28WATER
->47,29LAND ->48,29LANDavoid48,28antimagic ->49..56,29 ->57,28WATER ->58,27 ->57,26LAND
->61,26LAND ->62,25/24 ->62,23 ->63,23 ->63..66,22LAND ->67..70,22WATER ->71,22LAND
->71,19 ->71/72,18LAND ->73/74,18WATER ->UP75,18LAND. CHECKnewenemies/petswithtelepathy.
**KRAKEN9..10,17..19** nearD25down avoid; southernrouteavoids. NewE11,18unidentified,
peaceful? redDragon16,21old maywander,newO76,18 nearUPmustinspectbeforecrossing.
**PRAYER STILLUNSAFE TYRANGER1**. NearestaltarD19 17,12 needfreshcoalignedsacrificeatonement.
OBS22:58:39active0drops/reconnect/congestion. NO USERSTOP. CONTINUEPLAYINGLIVE.

OLDER:
LATEST T22234 D28 HERO43,19 **DOWNSTAIRS toCASTLE D29UP7,19**. HP119/119 AC-10 XL12/33885 KOFF.
**PET XORN ADJ6,19 beforeascending22234, shouldfollow; verifytelepathy**.
**CASTLE UP7,19 FOUND UNDER BOULDER via#terrain**. W DIGGING1use222? actually22052 dugWALL8,19,
thenpushedboulderto8,19 then9,19; boulderstill9,19. NEW SHORTCUT UP7,19->8,19->SE9,20->SE10,21courtyard.
CAUTION8,19 adjacentPOOL9,18 sharkbite; neverpetswapFROMwater. Stair7,19safe.
**F OLD DIGGING EMPTY5uses, droppedON D29UP7,19 T22053**; Wdig1use now. eotherdigunused.
**WESTMINOTAUR polyY5thuse22018->BABYGREENDRAGON killed22020**. Y5total,R5,Bcancel1left.
Minotaurambush22017 HP109->66, nowfullyrecovered. Boulder7,13 alsoPOLY->FREEZINGSPHERESTATUE.
LANDMINE5,15 triggered22007 ->PIT, legwoundhealed22055 Dx17restored.
ANTIMAGIC(?)7,25 trap 'sluggish'3HP; bypassvia6,25 whenpossible.
Westmaze courtyard5,23->5,24->SE6,25(bypassboulder5,25)->7,25->S7,29->W5,29->N5,27->W3,27
->N3,17->E5,17->N5,15PIT->E7,15->S7,18->SW6,19->UP7,19. Northwest7,14->6,13->4,13
->SW3,14->3,15deadend. Southwest3,29deadend. UPunderboulder7,19 nowuncovered.
**g HEALING unknownBUC MAINPACK**, retrievedfromo21984; **o now30items INSIDE y**; allotherbagcontentsunchanged.
Additionalhero kills giantant4,27T22042; WATER ELEMENTAL9,23T22084;
soldiers10,22T22081,9,22T22095,11,21T22104,8,19T22173. AllCastleothersremain.
PetXORNstilltameverified22143, finallycaughtup22233 afterlooteating, notabandoned.
Pwish(1:1)NEVERrechargeagain; kCastle0..2unknown1usedneverrecharged; pblessedcharging1reserved.
qpartlyeatenLIZARD remains, sSPEEDBOOTS worn,LwaterbootsOFF; PRAYERUNSAFE TYRANGER1.
OBS22:40:50active0drops/reconnect/congestion. UserNOstop, CONTINUEPLAYINGLIVE.

OLDER:
LATEST T21977 CASTLE D29 HERO21,19 HP98/119 AC-10 XL12/32831 KOFF NOTSATIATED.
**NEAR-STONING EMERGENCY RESOLVED**: OLOGHAI21,20 wieldedCOCKATRICECORPSE21971-73 hitus,
3attackbatch causedstiffening; **eq21973 curedthenreinfected; zY4T21974 polyOlog->GREENSLIME**,
slimedroppedcorpse; **eq21974 resumedlizardCUREDSTONE**, slimeattackmissinterruptedmeal;
**zR4T21975 killedGREENSLIME**. **NO STONE/SLIME NOW**. qLIZARDCORPSE PARTLYEATEN stillpack!
**Y POLYMORPH4usesNOW**, **R FIRE5usesNOW**. Bcancel1LEFTunchanged.
**V COCKATRICECORPSE picked21,20T21976 withuGLOVES worn, immediatelybaggedDIRECTy21977**.
DO NOT EAT V/cockatrice, DON'Thandlewithoutgloves. Don'twieldwhilemovingoverunknowntraps/falling.
**SMALLGLOBS greenSLIME andBLACKPUDDING onfloor21,20 LEFT, DON'TEATSLIME**.
**e NEW DIGGING wand unknownBUC picked21,20T21976**,0usesknown (monsterpossiblyusedunknown).
**E now4C-RATIONS** pack(1new21,20); **O FOODRATION packnew21,20**. A K-rationpack.
**PYROLISK21,19 killed21970 blind, NO CORPSEconfirmed21977**. StillNOFIRE/SHOCKres.
Stoning 'slowingdown' possiblyremovedINTRINSICspeed, sSPEEDBOOTS stillWORNveryfast.
Currentfullfood: qpartlyeatenlizard,hroyaljelly,Tcookie,AK, E4C, Ofoodration +1foodrationinsideo.
PetinvisibleXORN last27,17T21970 alive. GUARDRAIL scoutmonsterWEAPONespTrollbeforemelee!
**OLOGHAI dangerousdead viapoly**, oldWESTMINOTAUR7,18 alive,giantEELS13/14,18 etcalive.
Headingwestcastleentrancevia19,21->15,21->DRY14,21->courtyard. NeedUPD29stillunfound.
**WearLwaterboots beforeanywater, currentlysSPEED**. NeverpetswapFROMwater.
OBS22:05:00lastactive0drops. USERNOstop continueLIVE.

OLDER:
LATEST T21960 CASTLE D29 HERO36,18 HP119/119 AC-10 XL12/32443 KOFF **NOTSATIATED since21889**.
**Speedbootss+0WORN**, LwaterbootsOFFpack NEVERPOOLwiths. Pwish(1:1)reserve NEVERRECHARGEPagain.
kCastlewish1usedremaining0..2UNKNOWNnevercharged, pBLESSEDcharging1savedforit.
**B CANCELLATION NOW1CHARGELEFT**, lastzB6T21931 at35,18, secondDISENCHANTERkilled21934.
FirstR49,16killed21856. PotentialthirdRnotseenlasttele21917, maybe2total? Don'tassume.
**PURPLE-RED POTION=HEALING formallyID21900** ogrekingdrank'looksbetter', verifiedsrc/muse.c.
OldoSACKcontains1CURSEDHEALING+1UNKNOWNHEALING (formerlypurple-red), needtakeusefuloneoutsoon.
**yBOHcontains oOILSKINSACK31items +randomGEM +NEW C TELESCROLL +NEW H MURKYPOTION +1280GOLD**.
Allpreviousoitems stillinsideincluding3520GOLD, TOTAL4800gold now. B wandoutsidealways.
**A K-RATION PACK** picked60,16T21895. **E 3C-RATIONS PACK** 1at53,16T21907+2at48,16T21911.
**M HAWAIIANSHIRT unknownBUC PACK** picked36,19T21941. Don'twearuntilBUC/saferemovearmor.
NEWCtele unknownBUC from60,16bagged21897, adds3rdtele total2insideo+1directy.
NEWHmurky unknownBUC48,16bagged21912directy (oldUNCmurkyinsideo remains).
**NORTH BARRACKS BOX28,18 UNLOCKED EMPTY**, checked21946, looted21948.
**NORTH BARRACKS CHEST25,19 UNLOCKED, YELLOWGEMONLYLEFT** checked21950,1280goldtaken21952.
Allnorthbarracksinitialsoldierscleared; **lastSERGEANT36,18 killed21960** (wounded21917).
**TITANOTHERE36,19 dead21939**, corpse36,19nutritionmaybeoldsoon, shirtMfromsamefloor.
**INVISIBLE XORN PET alive** lasttele21917 at21,16, unNAMED. visiblepetdead21738.
**4CASTLEDRAGONS STILLASLEEP** gray56,18 gray56,19 yellow56,23 black56,24 confirmedtele21881.
NoFIRE/SHOCKres, reflect/MR/disintyes. PRAYERUNSAFE Tyranger1, needaltaratonement.
**Additionalkills21885..21960**: soldier62,16T21885; sergeant62,16T21887;
soldier62,16T21889; lieutenant60,16T21892; soldier60,16T21894;
ogreking58,16T21900; sergeant53,16T21904; soldier48,16T21910;
soldier35,18T21930; R35,18T21934; soldier35,18T21936; soldier36,18T21937;
titanothere36,19T21939; sergeant36,18T21960. 17+earlierkillsthisCastle.
Yellowlightblinded21917 curedax21918. Noongoingailment.
CurrentthronepeacefulG37,19 H39,19 N41,23; hostileOGRE45,19; otherpeacegiantnotvisible.
SOUTH BARRACKS25..34,23..24 stillpacked~19soldiersuntouched. Don'topen35,24yet.
THRONECHEST46,21unsearched, stillneedchecktraps. Storeroomsunopened4dragons.
Nextintentroutebackcastleentrance ->findUPD29(westmaze), orlootthronechestfirst. D19altarnearestknown.
NE67,15CURSED SCARE +BURNED ELBERETHsafehealingrefuge; NWtowerempty.
OBS21:51:38active0dropslastcheck(~10minoldsoonrecheck). USERNOstop CONTINUELIVE.

OLDER:
LATEST T21881 CASTLE D29 HERO67,15 NE WISHCHEST, HP119/119 AC-10 XL12/29810 KOFF SATIATED.
**CASTLE WISHING WAND FOUND k**,1wishused21873 for2BLESSEDCHARGING p(TEMOV).
**P OLD WISHING rechargedONCE21874 ->(1:3); 2WISHESUSED ->(1:1) CONFIRMEDinventory21881**.
**NEVER RECHARGE P AGAIN**, keep1wishreserve. kremainingUNKNOWN0..2 NEVERRECHARGED.
**p 1BLESSEDCHARGING reserved for k AFTERempty**. NeedIDk so don'triskprematurewrest.
**s NEW SPEED BOOTS WORN, +0** wishblessedfixed+3 nothonored+3butbootswork. BUC/erosionproofrequestednotformalID.
**L WATERWALKING BOOTS NOWOFF, carriedpack**, NEVERSTEPPOOLwiths! ACstill-10, veryfastspeednow.
**y NEW BLESSED GREASED BAGOFHOLDING**, wish21876; containsrandomGEM plus**oOILSKINSACK WITH31ITEMS**.
**o nowINSIDEy!** alloldbagcontentsandinnerordinarysackunchanged. Takeooutbeforeaocommands.
**B CANCELLATION OUTSIDE BAGALWAYS**, NOW(0:2) confirmed; lastzB6 from48,16T21853disenchanter49,16.
**Disenchanter49,16 KILLED21856**, noExcaldrain. Other2Rremainunknown/cancelledstatus.
**PRATYAVAYAH=SCAREMONSTER**, cursedscrollonfloor67,15 LEFT. BurnedELBERETHsamefloor.
**Chest67,15 UNLOCKED EMPTY**, castlewishingchestguaranteeduntrapped. DO NOTATTACKFROMHEREbreakElbereth.
Soldiers(>=5)approachupperhallfromwest, last@62/64,16. TheyTURNTOFLEE fromSCAREscrollhere.
**NW TOWER11..15,15..16 EMPTY no chest**, fullyseen. NEtower65..69,15..16 SAFErefuge.
RouteNE ->door64,16 ->longhall17..63,16 ->brokenNdoor41,17 ->throneroom.
**Newkills since21774**: soldier34,21T21776; soldier37,21T21782; soldiers29,16T21797,
27,16T21800,26,16T21803,20,16T21808; LIEUTENANT21,16T21823; soldier26,16T21828;
SERGEANT39,16T21841; summonedETTIN39,16T21844; disenchanter49,16T21856.
Effervescentpotion=ACID (called21847) thrownhero3damage. StillnoFIRE/SHOCKres.
PeacefulSTONEGIANT andFIREGIANTthrone; peacefulGNOMELORD41,16/39,19; goldennagapeaceful.
LastpetINVISIBLEXORN aliveearlier, unseenlong, NOdeathmessageheard. Visiblexornpetdied21738.
WandcountsRfire4 Fdig5 nstrike3 Ypoly3 Wdig0 Gtele2 Xtele0 B2LEFT P1:1 kunknown1used.
PrayerUNSAFEanger1. Noatonement. NeedD19Tyraltarornewcoalignedaltar. UPD29UNFOUND.
OBS21:38:46active0dropslastcheck. USERNOstop, KEEPPLAYINGLIVE.

OLDER:
LATEST T21774 CASTLE D29 HERO33,21 HP119/119 AC-10 XL12/27760 KOFF SATIATED.
Soldier34,21 adjacent, firegiant36,21 likelyPEACEFUL (atleastonefarlookconfirmed21764).
**VISIBLE XORN PET DIED21738**, INVISIBLE XORN PET ALIVE, lastentrance16,21.
**BURNED ELBERETH12,21 T21703 Rfire4thuse**, refuge, don'tattackfromit; humans/minoignore.
8SOLDIERS killedtotalhero; last3 at25/27,21 T21762/64/68.
HUMANMUMMY17,20dead21747, HUMANZOMBIE18,21dead21749, oldcorpsesDONOTEAT.
PetkilledTROLL15,21T21766 thenPICKEDUPCORPSE21771, mayrevive; leprechaun16,20dead21771.
PeacefulGOLDENNAGA leftcorridor21759, nowN43,20 another/one. PeacefulSOLDIERwestcourtyard.
Rdisenchanters17/18,21 behind, 2likelycancelled B21645, thirduncancelledunknown.
Entrance16..23,18..24 fountain19,21; open24,21 ->corridor25..34,21 ->open35,21 ->throne36..46,18..24.
THRONE45,21 CHEST46,21 ordinarynotwishguarantee; cornerTOWERchesttargetstillUNFOUND.
SeekNdoor41,17 ->upperhall41,16 ->west/easttowers; giantpeacefuldon'tattack.
Rfire4used Bcancel3LEFT Fdig5 nstrike3 Ypoly3 Wdig0 Gtele2 Xtele0 PwishEMPTY0:0unrecharged.
PrayerUNSAFE Tyranger1; nofire/shockres; disintres/reflect/MR yes. AllLgenocided.
OBS21:23:24active0drops. USERNOstop, CONTINUEPLAYINGLIVE.

OLDER:
LATEST T21693 CASTLE D29 HERO12,21 ON ELBERETH dust21650. HP78/119 AC-10 XL12/27180 KBLINDFOLDON SATIATED.
RESTING recover119. **DO NOT ATTACK FROM ELBERETH**, humans&minotaursignoreit.
**NEW TWO TAME XORNS** oneINVISIBLE! TamedZLORFIK21660, bothfarlookconfirmed.
**ZLORFIK=TAMING consumedlastUNCcopy21660** emergency, worked.
**SOLDIERpeaceful** formerattacker11,22 pacifiednotpet, last11,20. Don'tattackany@withoutfarlook.
**HAPAX nowAMNESIA byelimination** unknownBUCbag, DO NOTREAD, unnecessaryrisk.
Xornpetslast15,21(visible) and13,19(INVISIBLE), fightingcastlehostiles.
NewpetsUNNAMED; unlikeRelay NEVERswapfromwater/trap. HEROCURRENT12,21 LANDsafe.
Healthnadir44 fromsoldierignoringElbereth21659; tamingturnedcrisis, healed78now.
Elberethrepelsdisenchanters/ogres/xorns/trolls; don'tmoveoffuntilhealedunlessdanger.
MINOTAURwestlast5,21 separatedWALL8,21 routevia5,23->9,23->courtyardstilldanger.
OtherH40,16 &44,21 unknown (probablygiants butfarlookbeforeclose).
**B CANCELLATION3CHARGESLEFT**, used21645E from14,21 lined2DISENCHANTERS15,21and18,21;
noenchantmentlostdespitesubsequenthits, likelybothcancelled. ThirdR30,21UNKNOWN/uncancelled.
**XORN1 KILLED21647 at15,20**, other2tamed21660. 5SOLDIERS killed total; ICE TROLLkilled21644,
corpse15,21 leftpossibleREVIVAL (otherTpresent); anothericeT16,19 last21693.
PETSpotentiallyeatcorpse—butdon'tassume. Monsterwandstrikingstillunknowncarrier/loot15,21.
RemainingcourtmanyR/T/O/M/N/H/E plus4dragons56,18/19/23/24; armiesinbarracksmostlyuntouched.
R10,19 &11,21 localdisenchanters, O16,20ogre; peaceSoldier11,20, petsX15,21&13,19.
Westswimmers13,18+14,19+13,24+14,24 dangerousNOPOOLSWAP. Drybridge14,20/21/22safe.
Rfire3used,Fdig5used,nstrike3used,Ypoly3used,Wdig0used,Bcancel3left.
Pwish0:0EMPTYnevercharged, newCastlewishwandUNFOUND. Nospeedboots/nofire/shockres.
OBS20:59:32active0drops (~4minold). UserNOstop, CONTINUELIVE.

OLDER:
LATEST T21641 CASTLE D29 HERO14,21 DRYLAND choke. HP95/119 AC-10 XL12/26562 KOFF SATIATED.
FOUR SOLDIERS KILLED21632/34/37/41 at15,21; NEW SOLDIER15,21 active,
another17,22; hostileXORNS17,21/20,21 oneINVISIBLE; OGRE17,20; ICETROLL18,22.
**DISENCHANTERS >=2** formallyfarlook21,21/23,21, movedinsidehall; NOTCANCELLED.
**B cancel4chargesleft**, save fordisenchanters. DO NOTMELEEuncancelledR withExcal.
**DRY MOAT BRIDGE14,20/21/22** createdBLESSED EARTHscroll21630(LOREMformallyID).
Herostanding14,21 safeLAND now;15,21doorway ->16,21hall. Besthold14,21bottleneck.
BOULDERS12,20/13,20/12,22/13,22; boulder12,21 SHATTEREDenemystrikewand21637.
**DRAWBRIDGE DESTROYED nSTRIKING3rdcharge21617** from12,21safedistance.
GiantEEL14,20 killed21621 +1076XP; SHARK14,23 killed21624, bit20+18HPnadir81.
OtherWestswimmer giant/shark remainsNmoat11,18last21624 andSW10,29last21624.
3HILLORCSdead21610/12/14 at6,23and9,22. Helm9,22LEFT, corpsegear6,23LEFT.
**R FIRE now3chargesUSED** 2shotscastle21626/27 damagedsoldiers, noimmediatekills.
**OLD sFIRE EMPTYconfirmed21628**, dropped13,21 thenenemystrikewandSHATTERED21637.
**BLESSEDEARTH CONSUMED21630**, UNCearth remainsbag. Nootherresourcesused.
EnemywandSTRIKINGat15,21 lootpilepassedbetweenSOLDIERS, latestcarrier15,21alive.
PwishEMPTY0:0unrecharged stillpack; CastlewandwishUNFOUND, target4corners.
NoUNDEAD/LICHESallLgenocided; T/R/X/O/N/H enemycourtstillmany.
MINOTAURwestmaze~7,18 last21624; 2cockatriceclasswest, avoidbarehandcorpse.
PrayerUNSAFE Tyranger1(noatonement), nofire/shockres. OBS20:43:54last0drops(~8minold).
USERNOstop. KEEPPLAYINGLIVE.

OLDER:
LATEST T21610 D29 CASTLE HERO5,23 HP119/119 AC-10 XL12/24742 KOFF SATIATED.
FELL viaD28TRAPDOOR at~38or37,15 T21606 whileG4from39,15. D28DOWNunknownstill.
D29landing5,23 ->eastorcapproach x6..12,23 ->MOAT14,23 WALL15,23.
DRAWBRIDGE#15,21. 3HILLORCS here:firstkilled21610, secondadjacent6,23.
Telepathy21607: COCKATRICE6,21confirmed; c4,27unknown; MINOTAUR7,14confirmed.
Castlewestguards @11/13,16 &11/13,26; east65/67,16 &65/67,26.
Mainhallmanysoldiersx16..20,y18..24. Barracksx25..33y18/19/23/24 fullsoldiers.
ThroneroomT/X/O/H/R/N/C/m x36..45,y19..24, unknownspecies.
4DRAGONS56,18/19/23/24 unknowncolors. Giant eelsmoat14,20/23 &66,20/22,
sharks13,13/29 &65,13/29. q73,16unknown. No stairsfoundD29yet.
CastleNOTELEPORT,NONDIGGABLE. Wandofwishing random4cornertowerschest, UNTRAPPED,
Elberethburned+cursedscaremonsterscroll onfloor. Source dat/castle.des3.6.7read.
HavevOPENINGwand tolowerdrawbridge or nSTRIKINGtodestroyFROMDISTANCEsafe.
NOFIRE/SHOCKRES, intrinsicdisintres+reflectionamulet+MRgrayDSM. qlizardcarried.
**Fdig5chargesused** last21588 openedSHORTCUT46,21 joins47,21to45,21D28.
D28newnorthcentralroutes53,17->S53,19->W49,19, S49,25DEADEND;
W49,21->47,21DEADEND untilnewdigshortcutwest46,21.
N49,19->49,15->W45,15DEADEND, E49,17->51,17DEADEND.
Leftcenter via45,19->46,19LEVELTELETRAPMRblocked->47,17->44,17->43,16->43,13.
W43,13->41,13->S41,15->W39,15(gold30140,15LEFT); nextG4FELLCASTLE.
S39,16D28unexplored. LastOBS20:43:54active0drops. USERNOstop continueLIVE.

OLDER:
LATEST T21558 D28 HERO53,17 headingS53,18 unexplored. HP119/119 AC-10 XL12/24727 SATIATED KOFF.
E55,17 entireCENTERPOCKET mappedDEADENDS, noDOWN. RAVEN62,23 killed21515.
NEW TELEPORTSCROLL eunknownBUC bagged21510; pburntELVENDAGGER DROPPED61,25tomakeroom.
BOULDER57,25 immovableSouth, bypass57,24->56,25west or58,25east.
Route57,24 ->58,25 ->E61,25(daggercache) ->N61,23 ->E63,23:
N63,19DEADEND; S63,25->E65,25->N65,23DEADEND.
Westboulderroute56,25->W53,25->S53,27->E55,27DEADEND.
N55,25->55,23DEADEND. N57,23->57,21DEADEND.
ReturnedviaTRAVEL55,17, thenW53,17current; S53,18new.
Otherunexplored: E57,29; W55,13; W43,13; variousWEST<43oldbranches.
OBS20:34:26active0drops, userNOstop. ContinueLIVE.

OLDER:
LATEST T21501 D28 HERO57,21 DEADEND northspur. HP119/119 AC-10 XL12/24679 KOFF SATIATED.
Nhelm nowTHOROUGHLYRUSTY blessed+1 WORN; rustmonster2rust21478/79,
RUSTTRAP61,16 thirdrust21488. Helmoff/on done. Othergearunchanged.
TITANOTHERE60,19 killed21477; RUSTMONSTER60,19 killed21480;
3SOLDIERANTS dead21482/83/85 near60,19 &61,18. No wandchargeused.
60,19corpse/slimemolds LEFT. Newroute55,17 ->E57,17 ->S57,19 ->E61,19.
N61,19 ->61,15 DEADEND withRUSTTRAP61,16. W61,17 ->59,17DEADEND.
S61,19 ->61,21 ->W59,21 ->S59,23 ->W57,23.
N57,23 ->57,21 DEADEND(current); S57,24GOLD leadsunexplored57,25 next.
West55,17 stillunexplored. DOWNnotfound. ContinueLIVEuntiluserstop.

OLDER:
LATEST T21467 D28 HERO55,17 HP119/119 XL12/24225 AC-12 KOFF SATIATED.
DOWN still missing. Current junction E/W55,17 unexplored. UP6,21.
Route69,29 ->W65,29 ->N65,28(LENSESLEFT) ->NW64,27 ->W57,27
->S57,29 ->W51,29 ->N51,23 ->E53,23 ->N53,21 ->E55,21 ->N55,17.
E57,29 stillunexplored. LIZARD74,29 killed21431 corpseLEFT; qsparecarried.
Telepathy21460: WESTMINOTAUR20,15; newY19,16/S9,17/k64,13unknown;
ants14,15/11,22unknown; bugbear14,29; rockpiercer10,23;
NURSE46,23 confirmed, RAVEN51,19, RUSTMONSTER53,27, TITANOTHERE57,24;
SOLDIERANTS55,23/55,25/53,26, unknown:48,27. Allmobile.
OBS20:27:35 active0drops. UserhasNOTsaidstop, continueLIVE.

OLDER:
LATEST T21417 D28 HERO71,27 SEDEADEND. HP119/119 XL12/24175 AC-12 KOFF
SATIATED disintegrationresnew. Travellingback69,29 via `_@11.` next.
**NEW X TELEPORTWAND** unknownBUC unused picked67,26T21380 fromblackdragonloot.
OldGtele2usedstillpack. **BAGINNERsack oldXletter willreassign**, don'tconfuse.
Ogre68,27lootclub/145gold/redgem/egg/tripe/allLEFT corpseoldnow.
**FOODRATION71,29LEFT**. S69,25DEADEND actuallynorthspurfrom69,27.
Route67,26 ->68,27 ->69,27 ->S69,29 **WEST69,29UNEXPLORED**.
E69,29->77,29->N77,21->W75,21->N75,19: W73,19DEADEND,E77,19DEADEND.
S75,21->75,27->W71,27DEADEND (current). **ALLSEbeyond69,29Echecked noDOWN**.
Returnto69,29 thenWEST. Noenemiesencounteredsinceogre21228.
Otherunexploredbranches listaboveoldnotes, DOWNstillnotfound. Noresourcesused.
UserhasNOTsaidstop, KEEPPLAYINGlive. OBSlast20:01:40active0drops (~8minold).

OLDER:
LATEST T21378 D28 HERO67,26 HP119/119 AC-12 XL12/24175 KOFF **SATIATED**.
**NEW INTRINSIC DISINTEGRATION RESISTANCE** gained eatingBLACKDRAGON corpse,
"You feel very firm." Finished21378. **DO NOT EAT more whileSatiated**.
**BLACKDRAGON KILLED21318 at67,26**, Excal7hits, HPnadir80, no wanduse.
Corpse initially randomROTTEN21320 momentaryunconscious noHPdamage, resumed,
interruptedbyOGRELORD. **OGRELORD KILLED21328 at68,27**, originalmagictrap
escapee, oneExcalhit. Severalobjects68,27 notinspected yet (next3:).
**SMALLMIMIC KILLED21310 at67,24**, disguisedstatueblacklight, corpseLEFTold.
Routefrom69,20 ->NW68,19 ->W65,19 ->S65,21 ->E67,21 ->S67,26CURRENT.
Beyond S67,27 ->E68/69,27 visible, **N69,26 andS69,28 unexplored**.
Other unexplored **N69,18 from68,19** branch, likelydeadend69,17belowwall.
NO DOWNyet. All6orcsdead, NEminodead, blackdragondead, mimicdead, ogredead.
Westminoalive, 3soldierants,2westantsunknown,titanothere,rockpiercer,bugbear,
lizardclass&new@27,20 unidentified remain. Rescan beforeapproach.
Current resources WdigNEWunused; Fdig4used; Ypoly3used; CemptySLEEPcached65,14;
Rfire1used; oldsf ire7used; nstrike2used; Bcancel4left; Gtele2used; Pwish0:0empty.
No fire/shockres still! PrayerunsafeTyranger1, no pet. OBS20:01:40active0drops.
User hasNOTsaidstop. Continue LIVEplay, no final until stoprequest.

OLDER:
LATEST T21297 D28 HERO69,20 ->next7(68,19) HP119/119 AC-12 XL12/23322.
**WISDOM NOW12** exercised21285, otherstatsunchanged. KOFF. Lastmealorc21247.
All6originalHILLORCS apparentlydead: 3near64,15 earlier; fourth73,16T21278,
fifth69,21T21295, sixth68,19T21297. GearLEFT, noresources/damage.
**DOWNstillnotfound**. **OBS20:01:40activezero drops**, noUserstop.
Newroutefrom64,15 ->63,16(2weaponsPopup) ->64,17 ->E67,17 ->N67,15
->E69,15 ->N69,13 ->E74,13 **BOULDER75,13 bypass3->75,14** ->S75,15
->E77,15. N77,13DEADEND. S77,17 ->W74,17 ->NW73,16(helm)
->NW72,15 ->W71,15 ->S71,21 ->E73,21 ->S73,25 ->W71,25 ->N71,23
->W69,23 ->N69,20 CURRENT, NW68,19gear thenwestunexplored.
**OTHERUNEXPLORED WEST69,13** toward67; nootherbranchesalongthisroute.
Lasttelepathy21285: BLACKDRAGON67,25 &MIMIC67,24 (unidentified) behindwalls;
WESTMINOTAUR24,21; NEW@27,20 unidentified; rockpiercer10,23; bugbear13,28;
3soldierants50,17/61,21/59,22; 2westants15,20/17,21unknown; titanothere57,22;
OGRELORD60,29 woundedearlierescaped, couldregennow; lizardclass32,21unknown.
Wnewdigunused, Ypoly3used, CemptySLEEPcache65,14; allothergearunchanged.
UserhasNOTsaidstop, KEEPPLAYING/livebroadcast, NOFINAL.

OLDER:
LATEST T21247 D28 HERO64,15 HP106/119 AC-12 XL12/23277 KOFF (nextPK/rest).
**NORTHEASTMINOTAUR neutralized**: at65,14 tried Csleep21224 EMPTY nocharge!
Got hit27HP. zY3 POLYMORPH21225 transformed minotaur toSTEAMVORTEX, killed21228
after3Excalhits, took10heatdamage. **Y now3CHARGESUSED**. **C EMPTY SLEEP
DROPPED65,14T21230**. **W NEW DIGGINGWAND** unknownBUC unused taken65,14.
**3HILLORCS KILLED** first64,15T21230, next63,16T21234 and21238. GearLEFT.
**FIRSTORCCORPSE EATEN21232..21247**, interruptedtwice butfinished, lastmealnow.
Floor64,15tripe/orcishhelm/209goldLEFT. Orcishdaggers etc63,16LEFT.
**POLYMORPHTRAP62,13** underoldboulder, MRblocked21222. **BOULDERnow65,13**,
pushedfrom62,13. Bypass64,13->65,14 (don'tpushboulderfurtherneedlessly).
**LEVELTELEPORTTRAP46,19**, MRblocked21294 (actually21194); allteletraps
blockedbyAntimagic asconfirmed src/teleport.c, safeifunavoidablewhileMRworn.
Routefrom43,23 ->N43,21 ->E45,21 ->N45,19 ->E47,19 via46,19trap
->N47,17 ->W44,17 ->DIAG43,16 bypassBOULDER43,17 (untouched)
->N43,13 ->E51,13 ->S51,15 ->E55,15 ->N55,13 ->E57,13 ->S57,15
->E59,15 ->N59,13 ->E64,13 via62,13polytrap ->DIAG65,14 ->SW64,15current.
**UNEXPLORED SOUTH63,16** currentnear, routebeyondunknown. Otherbranches
WEST55,13towards53; WEST43,13; SOUTH43,18behindboulder43,17; belowrestold.
**BLACKDRAGON68,27** newlyspawned T21215 farlookconfirmed, noengagement.
**WESTMINOTAUR24,21 stillalive**, NEonegone. Ogregotaway~50,17last21215.
Titanothere55,23; threeants49,16/48,15/57,19 soldierantsmostly; threeorcseast
remainafter3killed. All gearunchanged exceptnewWdig/emptyCsleepcached/Y+1use.
Prayerunsafe Tyranger1, no activepet. OBS19:49:06activezero drops.
User hasNOTsaidstop. Continue playing and streaming; NOFINAL.

OLDER:
LATEST T21161 D28 HERO43,23 KBLINDFOLDON HP92/119 XP23048 XL12 AC-12.
Resting to recover. **MAGICTRAP43,26** blinded/deaf/summoned OGRELORD43,25,
WINGEDGARGOYLE42,27 and RECONNOITERESS43,27. Horn cured blind/deaf21144.
Gargoyle killed21146 (corpse42,27), reconnoiteress killed21153 no loot.
Ogre hit twice then SCROLLTELEPORTED away21150, latest51,19. HPnadir81,
no wand use. **TELEPORTTRAP39,27**, MR blocked21141; avoid via40,27->39,26.
**BOULDER45,27** pushedfrom46,27 then bypass46,27->45,26 (safe bothways).
**DOWNstillnotfound**. New route from27,20:
S27,25 ->E31,25 ->N31,23 ->W29,23 ->N29,21 ->E33,21 ->N33,19
->E35,19 ->N35,17 ->E37,17 ->S37,19 ->E41,19 ->S41,21 ->W37,21
->S37,25 ->W35,25 ->S35,27 ->E37,27 ->S37,29 ->E49,29 ->N49,27
->W46,27 ->DIAG45,26 ->N45,25 ->E47,25(GOLD31LEFT) ->N47,23 ->W41,23
with **UNEXPLORED NORTHBRANCH43,22 CURRENTLYAT43,23**.
S41,23->41,25->39,25: N39,23DEADEND, S39,27TELETRAP ->E43,27
->N43,26MAGICTRAP ->43,25 joins? unexplorednorth; avoidmagictrap!
Other unexplored37,29WEST;25,16N;23,14S;6,21UPWEST.
D28 minotaursT21161 H24,21 andH64,17 BOTHconfirmed. Soldierants47/48,21
and49,20, titanothere55,23. Rockpiercer10,23 bugbear13,26, otherantswestunknown.
Lastmeal20958C-ration, noHungry. Tyranger1 no prayer, no pet, no resourcesused.
OBS19:39:50active0drops. UserhasNOTsaidstop. Continue liveplay.

OLDER:
LATEST T21068 D28 HERO27,20 KBLINDFOLDON HP119/119 AC-12 XL12/22607.
UP6,21 ->D27DOWN10,14; DOWN notyetfound. MINOTAUR23,23 behindwall nearby.
Route UP6,21 ->7,21 ->7,17 ->9,17 ->9,15 ->7,15 ->7,13 ->27,13
->27,17 ->25,17 ->25,19 ->27,19 ->27,20. S27,21floor ahead.
Unexplored N25,16 from25,17 and S23,14 from23,13. Gold301 at27,19LEFT.
Other H64,15 UNKNOWN, ants15,17/8,29 &45,15/47,15/48,21 UNKNOWN;
rockpiercer10,23 confirmed, bugbear13,26 confirmed. Other east orcs/mimic/q.
No resource changes. Rfire1used, oldsf ire7used, Csleep5used, Ypoly2used,
Gtele2used, Bcancel4remaining. No fire/shockres, no prayer (Tyr anger1), nopet.
OBS19:31:57active zero drops. User has NOT said stop. Continue live play.

OLDER:
LATEST T21021 D27 HERO11,15 **DOWN10,14 found** (next7>), HP119/119 XL12/22607.
**TELEPORTTRAP11,16 AVOID** bydownroom. UP26,14. SHORTSTAIRROUTE:
UP26,14 ->24,15 ->W23,16OPEN ->22/21/20,16 ->19,15/20,15 ->18,15
->E17,15OPEN DOWNROOM10..16,14..16partmapped DOWN10,14. Gold16,16LEFT.
UPwestbranchS19/20,17unexplored possiblySWTHRONEROOM4..15,26..27; no needfight.
**k C-RATION EATEN20958**, lastmealnow. hJELLY/Tcookie/qLIZARDpack, oneFOODRATION
inbag. Rfire1used, Bcancel4, Pwish0:0 unchanged, NEWGENOCIDEV stillbagunknownBUC.
D27Easternloopsfullycheckednodownaltar: CHESTROOM E63,25->64,25/24/23/22/21
->63,21/20->62,20/19/18/17 ->W63,17OPEN BELLROOM64..72,15..18.
**GRAVE+BELL68,17** ordinaryleft. BELLROOM W63,15OPEN ->62..58,15 ->57,15
DIAG56,14 bypassBOULDER57,14; joinsNORTHROOM E48,13 (no otherexit).
NorthroomS35,17->35/36/37,18->37/38,19->38,20 joinsS42,17loop.
DWARFROOM W34,25 ->33,25/26 **BOULDER33,27** bypassDIAG32,27->31/32,28
->30,28 ->E29,28SECRETOPEN joinsFIREGENOCIDEroom. Alljustloops.
NoaltarD27found. SWTHRONEROOMunengaged. NEW R FIRE+V GENOCIDEimportantfinds.
Noactivepet, TYRANGER1 prayerunsafe remains. OBS19:12:05active0drops(lastcheck).
User hasNOTsaidstop. Continue playing and streaming.

OLDER:
LATEST T20938 D27 HERO63,25 atOPENeastdoorchestroom57..62,25..27. HP119/119
AC-12 XL12/22607 KOFF. **NEW R FIREWAND** unknownBUC found27,28T20815, picked
20816. **1CHARGEUSED20881** killedQUANTUMMECHANIC42,13 (hadteleportedhero20855
despiteMR; teleportattackNOTblockedbyMR, don'tassume!). OldsFIRE7usedstillcarried.
**NEW V GENOCIDESCROLL unknownBUC found25,26T20819 BAGGED**. DO NOTREADuntilBUC
known/blessed. **NEVER BLESSEDh genocide as dwarf!!** Lclassalreadygenocided.
**B CANCELLATION now4CHARGES**: brownpudding28,25 cancelled20809 killed20812
withoutsplit/armordamage. **E TRIPERation DROPPED27,28** tofreeweightforRfire.
GIANTSPIDER35,14 killed20877; JAGUAR40,15 killed20883; XAN27,15 killed20857
noinjuredlegs. COBRA56,26 killed20929. Noothergear/resourcechanges.
**D27UP26,14->D26DOWN39,14**. PEACEFULSASQUATCHroamsUProom25..28,13..18.
UP S26,19OPEN ->26,20/21->27,21/22->28,22/23/24->N28,25OPEN
FIRE/GENOCIDEroom25..28,26..28 nowcleared; tripe27,28left.
RoomE29,26OPEN ->30,26/25/24/23/22->30/31,21->31/32,20->32,19/18/17/16/15
->33,15/14/13->W34,13OPEN NORTHROOM35..47,13..16.
Northroom E48,13OPEN ->49/50/51,13->51..56,14 **BOULDER57,14** bypassDIAG
from56,14->57,15->58,15 (eastbeyond58unexplored). Quantumdead, safeuntilspawns.
Northroom S35,17OPEN unexplored (probablyloopsouth). S42,17OPEN->42,18/19/20
->41/40/39/38,20. N38/37,19loopunexplored. SOUTH39/40,21->38/39/40,22/23
->N40,24OPEN **DWARFROOM35..44,25..27**. N38,24SECRETfoundstillCLOSED.
**WEB41,25** HAPAXLEGOMENONscrollLEFTwouldburden; gold42,25LEFT. Peacefuldwarf
roamsroom. W34,25OPEN unexplored. E45,25OPEN->46/47/48,25->48..55,26
->W56,26SECRETOPEN **CHESTROOM57..62,25..27**.
HAPAXscroll56,26LEFT, CREATEMONSTERscroll57,27LEFT. **CHEST57,27 UNLOCKED
UNTRAPPED**, contentsFOODRATION+GREENGEM left. E63,25nowOPEN->64,25/24north.
NoD27DOWN/ALTARyet. SWTHRONEROOM4..15,26..27 24monstersincl3dragons untouched.
Noactivepet, TYRANGER1 prayerunsafe, lastmealPYTHON20691. OBS19:12:05active0drops.
UserhasNOTsaidstop, keepplaying/livebroadcast.

OLDER:
LATEST T20782 D26 HERO39,15 HP109/119 XL12/21923 KOFF, recoveringthenDESCEND.
**D26DOWN39,14**, OWLBEARCORPSEonit killed20779. **UP25,13**->D25DOWN7,18.
Route UP25,13 E27,13 ->S27,14..25 ->E30,25 ->DIAG31,24 bypassBOULDER31,25
->N31,13 ->E38,13 ->DIAG39,14 bypassBOULDER39,13 (doNOTpushbouldersback).
Initialboulder27,14 pushedto27,20 thenSHATTEREDby**nSTRIKING2ndUSE20739**.
**nSTRIKING now2CHARGESUSED TOTAL**. XORN28,19 killed20742 inwall.
PITVIPER26,25 killed20750; HILLORC39,16 killed20774, gear39,16LEFT;
secondPITVIPER39,16 killed20782. OWLBEAR39,14 killed20779.
**ARROWTRAP31,17** firedmiss20760, markedarrowfloor. Gold21131,20LEFT,
gems27,21/22/25 &31,19LEFT. Nofood/resourcegain, lastmealPYTHON20691.
RemainderD26unexplored: UPwest24,13 route; DOWNsouth39,17east40..unknown.
LivingINVISIBLESTALKER E23,16; LIZARD24,13; LONGWORM51,17 unidentified;
PEACEFULDWARFKING53,21, HILLORC37,25 lastscan. Noothernearbyhostiles.
OBS18:46:30active0drops. TYRANGER1 prayerUNSAFE, noactivepet, Bcancel5.
Continue untiluserstop (none received).

OLDER:
LATEST T20726 D26 HERO25,13 UP25,13->D25DOWN7,18, MAZEnew. HP119/119 AC-12
XL12/21229 KBLINDFOLDON. **MEDUSA KILLED20721 reflectedgaze whileBLIND**, opening
southdoor7,20 causedimmediatekill; STATUEOFMEDUSA7,18 onDOWN. No wandused.
MeleePYTHON38,28 killed20685, **HEROATEfreshcorpse20687..20691 lastmeal**.
D25 SOUTHROUTE complete:38,28 ->32,28 ->28,28 ->26,28 ->24,26 ->23,25
->15,25 ->10,25water ->8,23land ->7,21 ->UNLOCKEDOPEN7,20 ->7,19 ->DOWN7,18.
**No friendlyswaps from water!** Nagaoutsidepeaceful; blind promptsattackanswerNO.
D25CREATE MONSTERscroll9,23 LEFT (wouldburden). VENZARBORGAVVE51,27copyBAGGED.
Palace SOUTHSECRET16,24 foundCLOSED, otherLOCKEDDOOR11,22 leftclosed;
SOUTHMedusa7,20 OPEN now. KRAKEN pool9..10,17..19 remains, don'tclosepool.
Palace statue@18,20 touristnamedallanb; E12,18 unknown/statue?; q10,13unknown.
D25 babyREDdragon16,21 last20719 alive centralhall, nofirecorpseeaten.
Yellowadult8,14+3babies6/7,14/15 unengaged. PEACEFULblacknagasaroundpalace.
NOACTIVEPET; TYRANGER1 PRAYERUNSAFE unchanged. B CANCEL5charges, P WISH0:0empty
nevercharged. No furtherresourceuse exceptpythonmeal. OBS18:40:18active0drops.
D26 telepathy Y19,13 / E20,17 / :15,17 identifying; w51,17 h52,17 o47,20 o46,21
S27,22 S37,25 X38,25 unknown. Startmappinghere. NOUSERSTOP, keepplaying.

OLDER:
LATEST T20660 D25 HERO39,28 dryland KBLINDFOLDON HP119/119 AC-12 XL12/20482.
Level12 jellyfishkill57,25T20612 (maxHP+7). ALL6eastern/centralPYTHONS killed:
64,22 /63,22 /58,27 /56,26 /50,29 x2 latest20641. 6killerbees killed20646..55.
LASTKNOWN PYTHON31,28 approachingfrompalacewest, NOTCANCELLED. Awaitondryland.
**BcancelNOW5CHARGES**, onezB4from57,26T20602towards2pythons51/52,26nowbothdead.
NewUNKNOWNBUC VENZARBORGAVVEscroll picked51,27T20642 **BAGGED**20644, base100.
**ANTI-MAGICTRAP48,28** stepped20645minorHPdamageonly, NOspeedlost/Pwloss.
Southernroute island62,23->62,25->61,26->57,26->58,27->57,28->56,29
->49,29 island47..50,29/48..51,28/50..51,27 ->44,28water ->40/39,28land.
**j39,25 STATUEBLUEJELLY**, notmonster. PeacefulBLACKNAGAroamscentral53,23/54,24.
Eels ;60,16knownGIANT; ;37,21 and38,22 unidentified (onegiant/onejellyfish).
KRAKEN9,19 palace; Medusa7,18. Neww26,26 likelySTATUE, notidentified.
Newd36,14 likelySTATUE? nottelepathyobservedandstationary, unknown.
NOACTIVEPET, TYRANGER1 PRAYERUNSAFE unchanged. Lastmeal20291 notHungryyet.
OBS18:28:34active0drops. Keepplayinguntiluserstop. No stop received.

OLDER:
LATEST T20586 D25 HERO62,23 KBLINDFOLDON HP112/112 AC-12 XL11/19526.
Crossed southern route UP75,18 ->71,18 ->71,22 ->67,22 ->64,22 ->63,23.
PITVIPER66,22 killed20561, COBRA66,21 killed20562, garter67,21 killed20563.
PYTHON64,22 killed20567, PYTHON63,22 killed20584; corpsesbothdrylandleft.
Third PYTHON badlywounded fled59,26 alive20586. GARTER62,23 killed20586.
Other S53,23/53,24/47,22/47,23/52,19 unidentified. GIANTEEL60,16 staysaway;
unidentified ;53,18/38,20/38,22, KRAKEN10,19. MEDUSA7,18 asleep.
Continue SOUTHARC via island60,27 towardswestpalace, avoidwaterwrap.
NOACTIVEPET, TYRANGER1 PRAYERUNSAFE remains. Noextra wandcharges since20548.
OBS18:20:43 active0drops, lastmeal20291 notHungry. No userstop.

OLDER:
LATEST T20548 **D25 MEDUSA VARIANT4** HERO74,18 ONWATER **L WATERWALKINGCONFIRMED**
bywalk74,18T20545 no drowning, calledwaterwalking. UP75,18->D24DOWN26,14.
**RELAY DROWNED20546 DIRECTHEROERROR**: hero74,18water moved6 ontoRelay75,18land,
swappedRelayintowater74,18. 'You drown Relay. rumble...feelguilty'. USERINFORMED.
**TYRANGER NOW1** (u.ugangr++), ALIGNMENT-15 perhack.c, PRAYER UNSAFEuntilSACRIFICE
atonement! HP112 AC-12 XL11/18874. NOACTIVEPET. LuckstoneZstilluncmainpack.
**tCRYSTALutility NOW3chargesUSED**, ztdownwhilehero74,18overpossibleRelaycorpse
20548 NOEFFECT. Couldbelocking/probing/nothing orcorpseabsent, no knownrevival.
PossibleRelaycorpseUNDERWATER74,18 notconfirmedexists/cannotpickupwaterwalking.
DO NOT EVER SWAP PET FROM WATER/LAVA/TRAP INTOIT. Deliberatecheckcurrenthero
terrain BEFOREnormalfriendlyswap, notjusttarget! Thisisnewcriticalguardrail.
Medusa7,18 TELEPATHYconfirmed. **O76,18 STATUEOGREKING notmonster**.
Dragoncluster7,14/8,14/7,15 probableyellowadult+babies; blacknagas/hatchlings
westpalace +central; numeroussnakesrandom14 inclnearby73,19 GARTERSNAKEidentified.
EELS ;60,16;38,22;43,22;28,27 plusKRAKEN10,17 initial. Needidentifybeforeapproach,
WRAPcanDROWN evenwaterwalking/levitation, nooilskincloak/grease. Bcancel6charges
canpreventNEWwrap (notnecessarilyreleaseexisting). TeleportlevelNOTELEPORT.
Primarydat/medusa.des variant4 geometryscreenOFFSET+3x,+10y (Medusaorig4,8->7,18).
PalaceNON-DIGGABLEorig1,1..22,14. DOWNunderMedusa7,18. PalaceeastIRONBARS20,18,
closeddoor15,18. ±areTREES. Allwatercrossshortmanualmoves, blindscanperiodically.
NElandnearUP: UP75,18/statue76,18; land71..75,19;69..72,18;tree70,17;71,17;
narrowland73,16->72/73/74,15->73,14->NEruinroom71/72,12 etc.
Primarysrcobjects bootsbase50=>speed/jump/water, nojumpspeed=>waterwalk nowproven.
D24 **DOWN26,14 insideLEPREHALL22..26,12..15**, SW22,16->23,17..21->SWroom23,22.
**VAS CORP BET MANI=CREATE MONSTER mechanically** leprechaunread20488 spawnedDUST
VORTEX25,15; killed20489fire. Ownbag3UNC+1CURSED+1newUNKNOWNBUC copies.
**s FIRE NOW7chargesUSED** +20488/89 eastleprehall. **n NEWSTRIKING1used20489**.
OCHREJELLY27,15 killed20489with2fire+1striking, corpse27,15LEFT (acidDONOTEAT).
2lepskilledfire20488/89, othersscatter. E27,15doorBURNTOPEN20488.
D24WATERPOTIONH BAG, ycramconsumed20291lastmeal. Allothergearunchanged.
OBS17:46:19active0drops. PublicnoteD25updatedexplicitRelaydeath/myerror/revivalfail.

OLDER:
LATEST T20486 D24 HERO22,15 LEPREHALL22..26,12..15, E27,15 JELLY identifyingnext.
Relay23,21 ALIVE eatingCROCODILEcorpse20484. HP112 AC-12 XL11/18257 KOFF.
CROCODILE killed23,21T20453. FLESHGOLEM22,25 destroyed20444, Relayatecorpse
immediately; NOHERORESISTANCEgain. STRAWGOLEM23,20destroyed20457.
SWroom actually19..25,23..28 (large); **ANTI-MAGICTRAP21,25**, **SLEEPGAS21,27**,
GRAVE20,25LEFT. **HARP25,23** triedaMimprovise20405 'harptwangs' ordinaryorEMPTY;
DROPPED20406 same25,23 toremoveBurden, NOTcarried. NEW H waterpotionstillBAG.
SWroomN23,22broken ->23/22/24,21 ->23,20/19/18/17joinsleprehallSW22,16.
SWroomW18,23broken->17,23/22/21->16..24,21loopN23,22. West16,21unexplored.
NoD24downyet. Leprehallentered20486; somelepsawake, chuggingpotionheard.
OBS17:38:20active0drops. Noextrawandcharges ormeals used.

OLDER:
LATEST T20395 D24 HERO20,28 SWroom19..?,27..28. **SLEEPINGGASTRAP21,27avoid**.
Relay19,28 alive, HP112 AC-12 XL11/17913 KOFF. **VAMPIRELORD** initialbat10,21
revealed20354 afterbatformkilled; destroyed6,17T20358 withExcal, nodrainlevels.
Rrustmonsterkilled17,23T20382 noarmorrust. Crocodile37,14onlyinitialotherhostile;
leprehall22..25,12..15 untouched withsomeawake butnogoldpack onlybag3520.
**NEW H potioncalledWATER** picked10,25T20373 BAGGED20374 unknownBUC.
D24 UProom3..7,12..15 armor3,12LEFT; HOLE6,14avoid; UP7,14.
E8,14broken->9..20,14; Nbranch12,13->12..9,12->E8,12OPENUProom loop.
Sbranch15,15->15/16,16->16/17,17(hidden17,17FOUND20330)->17..21,18
->20/21,17->20,16/15->20,14loop. LeprehallSW22,16broken joins21,17.
**UProom SECRET S5,16 UNLOCKEDOPEN20350** ->5/4/6/7,17->7/8,18/19
->9,19 ->N9,20broken FOUNTAINROOM7..12,21..25 fountain9,22LEFT.
Armor7,23LEFT, 126gold12,25LEFT, potion10,25pickedHwaternowbagged.
FountainE13,24broken ->14/15/16,24. **DIAGSQUEEZE16,24->17,23 IMPASSABLEpack**
searched8turnsnohidden16,23/17,24. NORTH17,23unexplored. S16,25/26/27/28
->17,28->W18,28broken NEWsmallSWroom19..?,27..28 sleepinggas21,27.
OBS17:29:47active0drops. LastmealCRAM20291 noHungry. NoD24DOWNyet.

OLDER:
LATEST T20312 D24 HERO7,14 **UP7,14 ->D23DOWN39,25**, Relay7,13alive KblindfoldON.
HP112 AC-12 XL11/17423 STR18/11 notsatiatedunburdened. **HOLE6,14 AVOID**.
TelepathyLEPREHALL22..25,12..15; colon37,14/B10,21/R65,22 identifyingnext.
**v formallyWANDOPENING confirmed20251 doorunlock, now3chargesUSED**.
**G silverTELEPORT called provenfloorobjectteleport20233, 2chargesUSED**.
**y CRAMRATION CONSUMED20287..91** (Hungrythen), currentherofoodfreshsafe.
D23DOWN39,25 room~38..40,22..25 notfullymapped; N39,21OPEN->39,20/19maincorridor.
**LargeBOX40,24 DISARMEDTRAP20287, UNLOCKED20292, EMPTY**. Gold38,25LEFT.
D23NWroom18..25,12..14 W17,13->16..14,13->14/13/12,14->12,15/16->11,16..19
->11,20maincorridor. S20,15opened ->20,16..23 ->20,24brokenUProom, loop.
D23 northbranch39,18 stillunexplored; noneednowdownfound.
OBS17:21:50active0drops. PublicnoteD24updated gear/newwands/Relay/wishingrecharge.

OLDER:
LATEST T20235 D23 HERO8,23 clearedWESTroom3..8,20..23. HP112 AC-12 XL11/17423.
ALL4GREYELVES killed20220/20222/20224/20229, Relay11,20 aliveeatingelfcorpse.
NEW **G SILVER WAND calledteleportation** confirmedmechanically: engravingvanished
20232, floorGOLD7,20teleported20233; cancellationalreadyBformallyID, invisnoobject
effectconfirmed3.6.7zap.c. **G2chargesUSED**, unknownBUC/remainingcharges.
NEW A unknownBUC VAS CORP BET MANI scrollpicked11,19T20226 BAGGED20227.
Elfgearcache11,19 includesmithril/leatherhelms/weapons/shield/ironhook, LEFT.
Elfgear11,20includesfadedpall/helm/shield/broadsword/whitegem/cookieLEFT.
WestroomE9,20broken->10,20->11..27,20maincorridor; E9,22broken->10/11,21loop.
Nbranch11,19->11,18 UNEXPLORED. Maincorridorbranch20,19/20,21 unexplored.
Northroom32,14south->31/30,15->30,16/17/18->27..29,18->27,19->27,20loop.
NoD23DOWNyet. OBS17:14:42active0drops. Lastmeal19198, ycrampackready.

OLDER:
LATEST T20184 D23 HERO32,13 KblindfoldOFF HP112 AC-12 XL11/16875.
Relay40,13 alive following. Giantbat32,14 killed20181, vampirebat32,14 killed20184.
Four approaching @ west: first25,13 formallyGREY-ELF; others20,17/20,18/23,20.
NORTHroom35..40,12..14 E41,12broken->42,12/13/14->43,14..19 mainshopcorridor.
WEST34,13broken->33,13->32,13->32,14 unexploredsouth. Gold36,12left.
NEW y CRAMRATION picked40,12T20172 inpack; noherofoodsinceD21ogrelord19198.
SHOPPAID20110 allno debt. gTELEPORTscrollBAGGED. BAGGOLD3520 loose0.
SOLD G emptyblessedoillamp5gold20120, A emptystriking75T20121, e emptycold88T20122,
allfloor48,20 nowshopstock. NOlamp now. nNEWSTRIKINGstillUNUSED.
vHEXAGONALwandbase150 engraving20126 noeffect, SELFzap20128 noeffect; 2chargesUSED.
LikelyOPENING/LOCKING/UNDEADTURNING; needsdoortestOUTSIDEshop, NOTcombatwand.
ConfirmedP WISHING(0:0) NEVERRECHARGED; B CANCEL(0:6); oOILSKINsack; ZUNCLUCKSTONE
mainpack; aBLESSED+2EXCAL. NOHOLYWATERleft. Nochargingknown/inshop.
Relay no longer mimic disguise since20155. ShopmimicsALL8dead, nohostilesleft.
Publicnote updated allpurchases, fullhealthAC-12Relayalive. OBS17:09:28active0drops.

OLDER:
LATEST T20109 D23 HERO57,20 INSIDEGENERALSHOP, paymentpnNEXT. **ALL8MIMICS
CLEARED**, Relay55,18 ALIVE mimickinglargeCAT aftergiantmimicmeal20100.
**HUGEIDENTIFICATIONS20066:** P UNC WISHING **(0:0) NEVERRECHARGED SAFEtocharge**!
Boneguesswaswrong. **B UNC CANCELLATION(0:6)** NEVERputinBOH; **o UNC OILSKINSACK**
notBOH. **XOR OTA formallyIDENTIFY**, oldUNCcopyV HOLYWATERblessed20065,
read20066 ID'dP,B,o. **LASTHOLYWATER O CONSUMED20065 NOHOLYWATERleft**.
ShopIDscrollW bought27gold20076 read20081 onnewZ => **UNC LUCKSTONE Z INPACK**!
Luckstonecost107 fromCHEST50,18. **GARVEN DEH=ENCHANTWEAPON** price80base60,
chestcopyXbought80 read20082 **aEXCALIBUR NOWBLESSED RUSTPROOF+2** (confirmedinventory).
Base lucklikely0 effective+3 nowluckstone, blessingfuturewouldhelp. NonewIDleft.
**$3885LOOSE beforefinalpurchase**, BAGGOLD0. Nextpn bill533 =>expected3352.
**NEWg SCROLLOFTELEPORTATION** unknownBUC bought133 floor58,20 (formallyIDalready
displayedbyshop). **NEWn WANDSTRIKING** unknownBUC fulluntested from58,19 cost200.
OldA STRIKINGEMPTY stillpack. **NEWv HEXAGONALWAND UNKNOWN** base150 cost200,
from57,20; needsENGRAVE-ID OUTSIDEshop afterpaying! AllwandsOUTSIDEBAG.
HP107/112 AC-12 XL11/16791 T20109 unburdened notsatiated. Relayalive, Circuitdead.
**SHOP D23TuktoyaktukPEACEFUL** room48..59,18..20 W47,19OPEN. ALLMIMICSdead20104:
49,20small20061;50,20giant20072;53,19large20087;55,18giant20090;56,19large20092;
56,20giant20096;55,20giant20098;59,20giant20104. Corpsefloor50,20eaten,55,18
Relayeating/mimiccat,53,19eaten,other56,19/55,20/56,20/59,20corpsesforsaleleave.
**CHEST50,18 unlockeduntrapped**, boughtGARVENscroll+luckstone; LEFTplainWATER7gold,
bluegem2667,violetgem800. **BOX53,18 unlockeduntrapped** LEFTfoodration60+2tripe40.
Otherstock: mottledspellbook51,18base100price133;darkgreenbook52,18base200price267;
unknownbook58,18;armor49,18/50,19/54,18(chainmail100)/56,18; potions49,19unknown,
52,20unknown,57,19BROWNprice133base100. Food54,19/59,19/53,20etcLEFT.
**VENZARBORGAVVEscroll57,18 price178base100LEFT**, ownCURSEDsameinbag.
Allotherfloorscrolls inspected ID52,19bought+read;tele58,20bought;49,20wasmimic.
NOCHARGINGHERE (no300scrollstock; allchestcontentsseen).
PRICEOWN: KOBATEoffer50=>base100; HAPAXoffer100=>base200; 2VERRYEDoffer100=>base100each;
XORoffer10=>base20ID. Allownedscrollsdeclinedsaleandpickedback,exceptIDconsumed.
Gamepricecodeconfirmed normalofferhalf (thiskeepernotdiscounted) get_costChar9
buy4/3 andunknownitemsometimes4/3extra; luckstone60 ->107 correct.
**D23UProom19..22,25..27 UP22,25**. PINKPOTION21,26LEFT weight, fortuneCOOKIE19,26,
LEATHERARMOR19,27left, **VAMPIREstatue22,27coversRUSTTRAP avoid**.
UPE23,26broken->24,26graffitiDigforvictory->24,25/24/23->25,23/22/21/20.
At25,20 W24,20unexplored leadswestroom3..?,20..21gold7,20.
E25,20->26..35,20->35/36,19->36..46,19 ->SHOPW47,19.
Branches26,19,39,18/20,43/44,18,othersunexplored. NoD23DOWNyetknown.
PublicnoteD23generalstore notyetnewluckstone/wish; OBS16:41:52active0drops.

OLDER:
LATEST T20018 D23 HERO21,26 near **UP22,25 ->D22DOWN36,16**. RELAY22,26 alive.
HP112 AC-12 XL11/15304 notsatiated/unburdened. Pinkpotion21,26 LEFT because
pickup wouldburden (answered n nextcommand). VampireSTATUE22,27 NOTmonster;
RUSTTRAP22,27 found20018 understatue. Avoid. **SHOPKEEPER peacefulTuktoyaktuk
48,19** telepathy; manyMIMICS49/50/53/55/56/59,18..20 shopprobablygeneral.
NeedreachshopforPRICE-ID of unidentifiedscrolls/potions/rings! Nootherminds
initialD23. Allgearunchanged, cshieldworn, Excalwielded, KblindfoldOFF.
**d LIGHT now10chargesused** extra19768D21fountainroom.
**JUYED AWK YACC formallyLIGHT confirmedread20010**, newfloorcopyH consumed,
twoUNCcopiesinbagnowformallyID. **NEW unknownBUC PURPLE-RED potionM** picked
D22floor37,18 20011 BAGGED20012 (extra toolderCURSEDpurple-redalreadybag).
D22UP49,15 (maybeactualstairs? heroarrival49,15) room45..?,12..15 incompletelymapped.
Wsecret44,13OPEN ->43/42/41/40,13->40/39,14->E38,14OPEN DOWNroom35..37,14..18.
**D22DOWN36,16 ->D23UP22,25** descendedRelay20016. DownroomlitwithLIGHTscroll.
E38,16broken->39,16 unexplored; S37,19broken->37,20/21/22->37,24..27 unexplored.
D22**PACKEDTHRONE/ZOO62..67,14..17 untouched** orcs,gremlin,troll,etc. Avoidifnotneeded.
Unidentifieds64,24 andm48,27 aliveleft. D22UProomS48,16closedunexplored.
**D21DOWN8,22 ->D22UP49,15**. Downroom4..9,21..25 partlywallsdugbydwarf.
**LEVELTELEPORTER6,23** NOTtrapdoor; peacefuldwarffellthrough19959, gone.
Leprechaunalive roamingdownroom, leftgold; spellbook5,23 andfood6,21 LEFT.
DownroomEopen9,23->10..14,23/24/25->W15,25UProom ->UP18,25.
D21fountainroom48..59,21..25, fountain53,22untouched. S59,26DUGbypass to59,27
longsoutherncorridor;boulder60,27immovableleft. Wsecret47,21CLOSEDunexplored.
N49,20OPEN->49..36,19 connectslandingcorridor. N59,20broken->59,19/18.
E60,23broken->61..64,23 plus61..64,24 loops->W65,22brokenEASTroom66..71,21..24.
Wsecret65,24CLOSED also samecorridor; EASTN66,20broken->66..59,19.
D21NORTHroom43..51,13..15, **SQUEAKYBOARD48,15 AVOID**, noitems/down.
W42,13OPEN->41..38,13->E37,13landing. Vampirebat37,13killed19822 corpseLEFT.
E52,14OPEN->53,14/15->54,15/16/17; S47,16broken->47..55,17->55,18/19
->56/57,18/19->58/59,19 connectsEAST/fountainN.
Xan58,25killed19763 hobgoblin19764 Relayatecorpse19765. Armor58,25left.
OBS16:19:53active0drops/congestion/reconnect; NOUSERSTOP keepplaying.

OLDER:
LATEST T19762 D21 HERO59,26 at newly DUG north opening of long southern corridor.
Relay59,27 ALIVE sole pet. HP112 AC-12 XL11/15039, unburdened, notsatiated.
**A STRIKING EMPTY confirmed19758, 4actualchargesused. F DIGGING now4used:**
19759 east through boulder didnotenablepush;19760 NORTH59,26 openedroomwall.
Boulder originally50,27 pushedto60,27 IMMOBILE; bypass via59,26 nowOPEN.
NewSEroomx~49..59,y~21..25 not fullymapped; xan58,25 HOSTILE hit2times19762,
hobgoblin57,24 halberdhostile approaching. Relay safelybehindhero.
D21UPE25,21 connects26/27,21->27/28,22->28..37,23 joins36,23centralN.
CENTRALS E39,25OPEN ->40/41,25->41,26/27->42..59,27 longcorridor.
Hiddenpassage49,27found19729. Boulderdigbypass59,26 from59,27 intoSEroom.
D20zoo FULLYCLEARED now: scorpion5,15 killed19667, smallmimic4,13 killed19672.
Smallmimiccorpse4,13left. Peacefulblacknaga leftroamingUProom. Allgoldleft.
D20DOWN5,13 (undergold) ->D21UP18,25 descendedWITHRELAY19695.
OBS16:06:39 active zero skipped/congestion/reconnect. Publicnote updateddeath
previously; old paragraph below saying requiresupdate is obsolete.

OLDER:
LATEST T19563 D20 HERO37,23 **CIRCUIT DIED~19550** sadfeelingmessage19552,
PK19553 confirmsgone and survivor29,26 identified RELAY. LikelyLEOCROTTA33,24
killedhim (lastfollowingroute, no fatalexchangevisible). **NO CORPSE FOUND
along33..37,24/23 corridor**, no revivalavailable. Userinformed. Noheropetattack.
LEOCROTTA sleptC19555 killed30,25 19557, Relayatecorpse19560. **C now5chargesused**.
RELAY solelivingpet, last30,25 eatingleocrottacorpse. ReturnforRelay thenD21.
HP112 AC-12 XL11/14818 Dx17 Wi11 Str18/11. NOTsatiatedsince19533, unburdened.
**E TRIPERATION new picked66,19 19449**, noldtripeconsumedtamingRelay.
R ONE FOODRATION stillBAG. 2foodcache66,20 someRelaymoved ->68,15; extrafood
still66,19 with3CHICKATRICECORPSES NEVER EAT. 2cache66,20 maybe1afterpetmoved.
Eastroom **68..77,14..19**, W67,18open ->66,18 ->66,19/20 southcorridor.
GRAVE74,14 leaveundisturbed. W67,15unlockedOPEN but solidwest, searched30NOpath.
**W25,25 smallSWroomOPENED19552**, connects24,25/24/23 ->23,22 northcorridor.
This gives shortcut fromSEviaSW26..30,24..26 toNWstairs5,13.
Bothdogs hadregrouped19477 thenCircuitdied19550. Relaycarriesthickspellbook
sometimes; latestspellbook55,27 droppedCircuit19517, another54,14 map+maybe
differentbook? Usernotinterestedinventoryjunk, leftallbooks.
PEACEFULblacknaga last17,14 19553; G46,19UNIDENTIFIED; manes41,19;
new s6,13UNIDENTIFIED bystairs beware. Smallmimic4,13sleepingstill.
Publicnote requiresupdate Circuitdeath; previousnoteincorrect2petsalive.

OLDER:
LATEST T19446 D20 HERO66,20 Circuit65,21 eatingrocktrollcorpse ALIVE, Relay
alsoALIVE lastfountainroom56,17~19422, followedpartway? NeedsPK tolocate.
**NEW SECOND PET RELAY** tame large dog at25,22 tamed19325 with nTRIPERATION
CONSUMED; namedRelay C m @9. RelaycarriedTHICKSPELLBOOK nowfloor54,14.
HP112/112 AC-12 XL11/14683 STR18/11 DxRESTORED17 Wi11. SATIATED.
**c SHIELD +3 and YPOLYWAND WERESTOLEN but BOTHRECOVERED19433, cREEQUIPPED19435!**
Woodnymph stolec19231, Y19317; usedY toSELF-POLYROCKTROLL19426, sleptC19427,
killed19432, lootedc/Y+2rations19433. **Y now2knownchargesused** (engrave+nymphzap).
**C SLEEP total4chargesused** (engrave+giant+succubus19241+troll19427).
**e COLD EMPTY confirmed19445**, total4chargesused engrave+2jelly19236/37
+chick19444. Emptyzap19445 didnotpromptdirection; trailing8 attackedchick.
**d LIGHT total9used**, Gempty. Allwandsoutsidebag BmaybeCANCELkeepout.
PEMPTY untouched stillonewishused rechargehistoryunknown preserve.
**R ONEfoodration nowBAGGED**, **2FOODRATIONS CACHEDfloor66,20** tofixburden.
Burdenended19443 afterdroppingextras. OuterbagdoesNOTreduceweight(enough),
likelyOILSKINnotBOH. Keepallfragilesbagged anyway.
**3CHICKATRICES KILLED66,19 19442/44/46; STONING CORPSES66,19 NEVER EAT!**
Heroheldchoke66,20 betweenCircuitandchicks. qLIZARDunused, NOstoningstarted.
**D20 DOWN5,13 IN NWZOO undergold ->D21UP18,25.** Horsehidstairs untilreturn.
HEROtrapdoorD20 **7,20 confirmed** fell19142; D21UPfound19225 returned19229.
Zoo now MOSTLYCLEARED: horse19233, ochrejelly19238 (engulf, 2coldcharges,
lowestHP62), bothsuccubi19240/45, ogrelord19243 Circuitate. Smallmimic4,13
ALIVEsleep, **BLACKNAGAPEACEFUL last10,14/6,15 roaming** CircuitbitbutheroNEVER.
AllzoogoldLEFT; stairs5,13 obscured bygold. NoheroattacksonElbereth.
Nymph initialstatslootconfirmed c/Y plusfrostgiantgems/quarterstaff/longsword.
**CACHE66,20:** 2foodrations, long sword, quarterstaff, mirror,3blue4orange4violet
4whitegems, Circuitdroppedknife. ROCKTROLLCORPSE eatenCircuit19437 ->no revival.
D20 ringroom **Esecret60,25OPEN** ->61/62/63,25 ->63,24/23 ->64,23/22/21
->65,21 ->66,21/20/19 ->door66,18 currentlylooksopen UNEXPLOREDroombeyond.
Nymphhadbeen69,18 beforepoly, chicks70,18/70,19/71,19 ALL3nowdead66,19.
FountainroomEwall59,14..18 searched15each NOdoor. Sstatue49,16stillUNEXPLORED.
NewG at49,15 seen19422 UNIDENTIFIED likelypeacefulgnome DO NOTblindattack.
Manesremaining23,20/15 area. Winterwolfcubs35,16killed19347 and43,15Circuit
killed19367 atecorpse19369; nootherknownhostiledogs now.
OBS15:38:11 active0drops. Publicnote updated recoveredloot/2dogs/D21next.
Currenttask finishescort/returnD21; optional explore66,18room ifsafe beforeback.

OLDER:
LATEST T19225 D21 hero14,25 UPSTAIRS FOUND18,25. Circuit STILL D20 alive last
15,14 eating freshrothe19126. HERO fell D20 trapdoor likely7,20 T19142.
IMMEDIATE PLAN: ascendD21UP18,25 to locate D20DOWN and return for Circuit.
HP112 AC-12 XL11/13206 STR18/11 Wi11 DxNOW16 (landmine19156). SATIATED from
fresh ogrelord killed19167 ate19168..98. BURDENED since landmine woundlegs,
unicornhorn19158didnothing. No armorchanges. Allgearworn/blindfoldOFF.
dLIGHT total9chargesused (D20NWroom19094 eighth +D21centralS19158 ninth).
D21 Greenelf34,13killed19144 corpse+fadedpall/broadsword/shieldleft.
D21 landingroom34..36,12..15, E37,13openUNEXPLORED, S36,16CLOSEDUNEXPLORED.
S34,16open ->34,17 ->36,17/18/19/20/21/22/23 ->N36,24 CENTRAL SROOM
34..38,25..28. **PIT36,26 fromLANDMINE triggered19156! avoid.**
Studdedleather34,26left, UNKNOWNFOOD38,26left, arrows+club36,25ogredropsleft.
E39,25CLOSED; W33,25openUNEXPLORED; W33,27unlockedOPEN ->32..15,27
**BOULDER14,27 bypassNW15,27->14,26->14,25**. Hiddenpassage29,27opened19208.
UPROOM16..24,21..25, UP18,25; W15,25open, E25,23closed, E25,21openunknown.
D21 initialtelepathy orc49,15 xan49,21 leprechaun8,23 allunidentified;
ogrelord22,21 killed19167. No Circuit onD21 at19145.
OBS15:17:43 active0drops. PublicnoteD21trapdoor seekingUPforCircuit.

D20 recent map: NW TREASUREZOO4..7,13..15 E8,15 ->9/10,15 ->10,14 ->13,14
->W14,14 room15..21,13..14. **NAGA6,13 PEACEFULBLACK**, leave! Zoo allsleeping
smallmimic4,13 horse5,13 blacknaga6,13 nymph4,14 OCHREJELLY5,14 yellowlight6,14
succubi4/5,15 OGRELORD6,15. Noheroattackszoo. Entered19117 left19118.
NWroomE22,13secretopened19091 ->23,13..22 junction connectsUPeastroute.
S16,15open ->16/15,16 ->15,17/18/19 +14,19/20 ->15/16,20 ->UPN15,21open.
UPN17,21 stillunexplored. UPsink15,24 revealed, noDOWNinUProom.
**UPN7,21opened19140 ->7,20 TRAPDOOR heroicfall19142** exacttrapcoordsverify.
Mimic50,15 killed19023. Manesgroup spawned19061 mostlyclearedalongroutes.
Rothes19,13 killed19097 Circuitate19100;15,14killed19104 and19125 Circuitate19126;
iguana13,14killed19106. Some manes stillalive nearNWroom.
D20 centralSE39..48,21..25 fullycheckedNODOWN. W38,23 ->35..37,23 ->32..35,24
->32,25 ->E31,25 smallroom26..30,24..26 gold26,26left NODOWN.
N45,20opened18952 ->45,19 ->44,19/18 ->43,18/17 ->41/42,17 ->N41,16SECRET
CLOSED tostatue. Branch44,19 W43..39,19 ->39,20OPENcentralroom.
E49,22open ->50,22/21 ->51/52,21 ->52,20/19/18 ->53,18/17 ->54,17
->W55,17fountainroom (loop). StatueS49,16 STILLUNEXPLORED.

OLDER:
LATEST T18943 D20 hero41,24 Circuit43,24 ALIVE reunited. HP112/112 AC-12
XL11/12792 STR18/11 Wi11. All armor worn, Excalibur wielded, blindfold OFF.
C LONG WAND now formally SLEEP: ray hit frost giant18856, total2chargesused.
d LIGHT now7chargesused (D20fountain18852 + centralSEroom18934). LampGempty.
D CORAL RING unknownBUC picked57,26T18922, unworn. BvanisherMAYCANCEL neverbag.
Frost giant killed18859, fresh corpse ate18860..68 randomrotten NOstrengthgain.
Warg18858, rockmole18875, barrowwight18906, glasspiercer18940 killed.
D20 UP6,22. DOWN UNKNOWN. UP E18,23 ->20,23/22 ->29,22 ->29,20 ->30,20/19
->31,19/18 ->32,18/17 ->33,17/16 ->38,16/15 ->39,15/14/13 ->W40,13
STATUEROOM41..49,12..15. Thickspellbook45,14left, rednagastatue43,14.
S41,16 and S49,16 open UNEXPLORED. E50,15 ->52,15/14 ->53/54,14 ->W55,14
FOUNTAINROOM56..58,14..17. Fountain57,15 untouched, BOULDER57,14.
Giantdrops55,14 gems+quarterstaff left; knife56,14 longsword56,15 left.
W55,17 OPEN UNEXPLORED. S56,18 ->56,19/20 ->57,20/21/22 ->N57,23
RINGROOM57..59,24..27. Ringcollected. W56,27 ->51..55,27 ->51,26/25/24
->50,24 ->E49,24 CENTRALSEroom current eastedge48 rows21..25 westUNKNOWN.
N45,20 CLOSED, E49,22 looksopenUNEXPLORED. Exploringwest now.
UP Nsecret7,21closed; N15,21 and17,21open UNEXPLORED; corridorN23,21unexplored.
NW telepathy stationary cluster m4,13 u5,13 N6,13 n4,14 &4,15 &5,15 O6,15
still UNIDENTIFIED leavecautious, iguana12,14. No other knownhostileD20.
Publicnote updated Circuitreunited/D20/sleepwand. OBS14:59:27 active0drops.

OLDER:
LATEST T18798 D19 chest56,15 checkeduntrapped+UNLOCKEDLOOTED. CircuitFOLLOWED
backUP18791 ALIVE besidehero57,15. New **n TRIPERATION**, **v HAPAXLEGOMENONscroll
unknownBUC BAGGED**, **y FIZZYpotion unknownBUC BAGGED** (outerbag28stacks).
New **B BRASS WAND called vanishes engraving** =>teleport/cancel/invis
1engravingchargeused18797; **C LONG WAND called sleep or death** 1engrave18798.
Both UNKNOWNBUC OUTSIDEBAG. **B mayCANCELLATION NEVERBAG IT**. Pemptyuntouched.
Chest56,15 STILLcontains MAGENTA SPELLBOOK+BLACKGEM left; notempty.
HP112 AC-12 XL11/12067 Wi11. ReturningD20withCircuit after chestcheck.
OBS14:41:39 active0drops. Continueuntiluserstop.

OLDER:
LATEST T18781 D20 hero9,23 Circuit10,23 REUNITEDALIVEtameconfirmed18773.
HP112/112 AC-12 XL11/12067 STR18/11 Wi11 (18600up). SATIATEDended18764.
D20 UP6,22 -> D19DOWN54,16. UProomlarge dark partiallylit, Nsecret7,21CLOSED.
HOSTILEGREYELF6,23 killed18778, corpsefresh floor6,23 mayCircuiteat soon.
ReturningUPbriefly to inspect D19 chest56,15. D20 onlysmallUPareaexplored.
D20 telepathy initial: NWcluster m4,13 u5,13 N6,13 n4,14 iguana7,14
&4,15 &5,15 O6,15; r44,21; H27,24; d46,25 ALLUNIDENTIFIED.
Circuit fell D19TRAPDOOR6,23 T18458 andfoundD20 19,23 alive18773, nowrejoined.
IguanaalsotrapdoorD19 fell18470 nowD20 likely7,14. NO PETDEATH.
d UNC LIGHT WAND now5 TOTALchargesused (engraveD17 + D19UP18455 +D19SW18723
+D19DOWN18771 +D20UP18774). G OILLAMP EMPTY. eUNC COLD1testused. PEMPTYunchanged.
bUNC CLAYring, jCURSED TIGEREYEring BUC D19altar1851x. gBRILLIANTBLUEpotion
UNC and X VASCORPBETMANIscroll CURSED (3UNC+1CURSED total) BAGGED18523.
**EMERALD=BLINDNESS formallyidentified** seenfloorpotionD19zoo45,22. OwnblessedBAG.
No other inventory changes sinceD18. Gold4099BAG+0pack; zoo goldLEFTall.
D19 **LAWFULTYRALTAR17,12** room16..19,12..14 W15,12 ->14/13,12/13/14
->12/11,14 ->11,15..20 ->10/9,20 ->9,21/22/23 ->E8,23UP room3..7,22..25.
**D19UP7,25**, fountain4,25, TRAPDOOR6,23 avoid, gold6,22left, Ssecret6,26closed.
Altar E20,13 ->21..28,13/14 intertwinedcorridors ->W29,14room30..41,14..16.
Altar S18,15 ->18,16..19 ->19,19/20 ->20,20..25 ->21..23,25
->N23,26 SWroom19..23,27..28 EMPTYnowlit. S22,29 ->22,30DEADsearched15.
SW Esecret24,28OPEN ->25..49,28 ->49,27..22 ->49/50/51,21/22junction
->51,20 ->52,20/19/18 ->W53,18 **DOWNroom54..??,14..19**.
**D19DOWN54,16, CHEST56,15 UNCHECKED, SINK57,15 untouched.** RoomonlyWpartlit.
Ncentralroom W29,16 ->28/27/26,16 (GLASSPIERCER26,16left) ->25,16/15
->26/25,14 joinsaltarE;26,17..21 ->26,22 ->25,22..28 joinsSWshortcut.
PEACEFULDWARFlast28,12seen18704 leavealone. NootherpeacefulnotedD19.
Ncentralroom S31,17 ->31..40,18 ->40/41/42,19 ->42/43/44/45,20
->N45,21 TREASUREZOO40..47,22..26. **STILLHALFFULLSLEEPERS**, notcleared!
Zoo E48,23 ->49,23 joinsaforementionedE/Souterloop. BOULDER52,21 bypassN52,20.
Killed zoo wolf45,22 (atefresh18620..30), ettinM46,22 (corpseOLDINHERENTavoid),
xan44,22, wolf43,22, wolf44,23, rockmole45,23, hillorcs46,23/46,24/47,23,
giantZ44,24, xorn45,24 (HP79lowest healed112afterrest). Quasit51,20killed18766.
Remainingzoo bugbear42,22; y41,22unknownlight; impminor i40,22/40,23etc;
BOULDER43,23; flesh?/othergolems '(42,24),(40,25),(44,25) UNIDENTIFIED;
rothe41,25, a43,24/25unknown; xan45,25; DWARFMUMMY46,25; E44,26unknown;
d42,26unknown; l41,26; f46,26unknown; @40,24unidentified. DoNOTblindattack.
ZOOallgoldleft; EMERALD BLINDNESS potionfloor45,22left+lotscorpse/gear.
D19 pyrolisk18,12killed18512 blindfold on, NOcorpse noFIREres. Homunculus31,16
killed18579; rothe33,18/36,18killed18589/91 corpsesnowOLD. Nothingeatenexceptwolf.
OBS14:34:32 active0drops. LIVE KEEPPLAYING untiluserstop.

OLDER:
LATEST T18432 D18 hero50,23 beside DOWN49,23; Circuit50,22 eatingSERGEANT183xx.
HP112 AC-12 XL11/10819 STR18/11 SATIATED. G OILLAMP EMPTY since18333.
NEW k C-RATION sergeantdrop, j TIGEREYERING unknownBUC from51,24. bCLAYring,
dLIGHTwand1used, eCOLDwand1used, fdagger allcurrent. NEW g BRILLIANTBLUEpotion
bagged18356 unknownBUC. Bag26stacks, 4099gold. P wishingEMPTY untouched.
**EMERALD POTION caused BLINDNESS when sergeant threw18423**, woreoff18424.
Not formallynamed yet, existing blessed emerald potion BAG so likelyblindness.
D18 UP27,21 room25..33,20..22 with W24,22 UNEXPLORED,
E34,21 ->35,21/20 ->36,20/19 ->37/38,19 ->38,18 ->39,18/17 ->40..45,17
->45,16/15 ->46,15 ->47,15Nroom48..59,14..16.
Nroom voulge49,14left; E60,14unexplored; S55,17 ->55/54/53/52,18
->52,19/20 ->51/50,20 ->50,21 ->Ndoor50,22DOWNroom49..51,23..25.
DOWN49,23, fountain51,23untouched, ring51,24collected. Esecret52,25nowOPEN
(hostilesergeantopened1842x). Sergeant74,26initially movedthroughEside
room andkilled18426door50,22, carriedflail+armorleftfloor, C-rationkcollected,
Circuit ate sergeantcorpse18428+. **WAIT for pet finishmeal beforestairs**.
Othertelepathy D18: killerbeehive61/62,25..28stillASLEEPLEFT; B batlast19,19
notidentified. Giantant49,14cameentrance35,21killed18363 Circuitate18365.
EscapedD17 HOSTILEGNOMISHWIZARD25,21 killed18354. Petblackgem28,22left.
D17 iceTROLL killed18335 Circuit ATECORPSE confirmed, entirethroneroomclear.
NEW SECRET UP-room Ndoor60,18 CLOSEDunexplored. D17otherbranchesstillunexplored.
OBS14:08:35 active zero drops. KEEPPLAYING untiluserstop.

OLDER:
LATEST T18286 D17 hero65,16 Circuit66,15 returning to throne room from NEroom.
HP112/112 XL11/10438 STR18/11 (fresh stonegiant corpse eaten18213..43), SATIATED.
AC-12 all armor Q/w/u/c/L/N/I worn, a Excal. f now +0DAGGER recovered42,26;
b now UNKNOWNBUC CLAYRING, d JEWELED WAND LIGHT 1 engravingchargeused,
e URANIUM WAND called COLD 1engravingchargeused. P empty wishing untouched.
Gold BAG4099 after chest1068. All old fragiles bagged. G lamp nearlyout18286.
D17 DOWN41,27 THRONE ROOM41..43,26..28; throne43,26, chest43,28 UNLOCKED EMPTY.
Throne guards killed hostile dwarfking18202 XL11, mountaincentaur18207,
hobgoblin18208, orcshaman18210, STONEGIANT18212 atefresh strength18/11.
HOSTILEGNOMISHWIZARD hit18212 fled DOWNSTAIRS alive expectD18.
ICE TROLL41,26 STILLASLEEP ALIVE. FetchingCircuit to eat corpse afterkill.
Throneroom entrance44,26 ->45,26/25 ->46,25/24/23/22 ->50,22/21.
UP54,20 room54..61,19..24; secret W53,21 OPEN ->51/52,21 ->50,21 junction;
N50,20/19 and W49/48,20 UNEXPLORED. W53,19 secret CLOSEDunexplored.
E62,19 OPEN ->63..65,19 ->65,18/17/16/15 ->66/67,15 ->67,14 ->68,14NEroom.
NEroom69..77,14..17 EMPTY with deadend closets71,12 via71,13 and
TELEPORTTRAP77,12 via77,13. Donotsteptrap. Secret northdoorsOPEN.
Naga peaceful gold lastUProom, neverattack. Circuit initiallyleftNEroom nowretrieved.
Lootleft: giant gems41,28 3black+3yellowbrown; armor43,26; corpsesoldforhero.
OBS13:59:45 active zero drops. Continue until userstop.

OLDER:
LATEST T18045 D17 hero54,24 on DUST ELBERETH, Circuit55,24. HP105 AC-12.
Read BLESSED MAPIRO MAHAMA DIROMAT => GENOCIDE, chose L. ALL LICH CLASSES
CONFIRMED EXTINCT including arch-liches. Scroll consumed. Armor safe, ALL
REEQUIPPED Q GDSM, w robe, u gloves, c shield, L boots, N helm, I reflection;
a Excalibur wielded. Temporary T auto-select caused cookie wield, corrected.
When only ONE worn armor, T auto-removes it WITHOUT letter prompt! No damage.
D17 UProom54..61,19..24, UP54,20, only CLOSED exit62,19. Distant throne shouts.
Telepathy18005 cluster T41,26 C42,26 h43,26 G41,27 o42,27 H41,28 o42,28.
P empty wishing still NEEDS ID/recharge counter, no charging identified.
All other scrolls/potions BAGGED. OBS13:49:42 active no dropped frames.

OLDER:
LATEST T18004 **D17** hero55,19 UP54,20 ->D16DOWN66,26. CIRCUITFOLLOWED55,20.
HP105/105 AC-12 XL10/9904 STR18/04. **R ONEfoodration remains** heroate17934;
triedfeedingCircuitR17894and17903 butmissed/notaccepted BOTHRECOVERED17904,
nofoodlost, nohero/petdamage; don'tassumeCircuitate. hONEjelly,Tcookie,qLIZARDunused.
**GblessedOILLAMP LIT refilled17533** Dark=OILpotionconsumed, ~800fueladded,
~470turnssinceleft~330ifestimatecorrect. KOFFbeforeD17survey. Excalwielded.
P WISHINGEMPTY UNC preserved0wishchargesleftunknownrechargecounter. Fdig2chargesused.
Allpotions/scrolls BAGGED; **NEW VASCORPBETMANIscroll X** D16floor63,26picked17645,
bagged17646 unknownBUC (3UNCpreviousbag =>4total), outero26stacksagain.
ONEHOLYWATEROstillbag. ArmorQblessed+0GDSM +wrobe, reflectionI. Gold3031.
D16DOWN66,26 room61..~69+,25..26 EedgeNOTfinished; Wdoor60,26.
PEACEFULGNOMISHWIZARDSElast69,25 LIVE (CircuitattackedbutheroDIDNOT), leave.
Circuitescortrequiredshortstages: EroomW56,19 gotstuckwrongsidewall57,20.
Going INSIDE57,19 then44444 linedpetoutside54,19. Stage45,20wait12 ->39,22wait10
->47,23wait10->50,26wait10->58,26wait8 ->stairs66,26. Avoidlongjumpacrosswalls.
WraithnotseenPKsince17344, likelyCircuitkilledbutnoactualmessage.
D16 NEW3APES northcorridors at177xx/179xx LEFT; CENTAURglyphC UProom23,20unknown
speciesleft, PEACEFULGNOMEKINGUProomleft. 3foodcache67,18 mayhavepetatenunknown.
NoD16altar, noIDscrollknown. AllknownroomsRoguevisitedexceptSEeastedge.
LIVE KEEPPLAYING untilUSERSTOP. LastOBS13:20:32(beforelatestcheck).

OLDER:
LATEST T17541 D16 hero15,21 HP105 AC-12 XL10/9904 STR18/04 UNBURDENED.
**G BLESSED OILLAMP REFILLED17533 and RELIT17534! DARK potion=d OIL identified
viaapply17532 (lit), snuffed ad17533 then #dipGd. OilPOTIONCONSUMED, ~800fueladded
(verifyexact). Wasgoneout1750x. G nowLIT3radius restored, keepusingnormally.**
R TWOfoodrations remain, ate1R17188. hONEjelly,Tcookie,qLIZARDunused.
ALLpotions/scrolls BAGGEDagain17541, outero25stacks(afteroilconsumed), innerX4potions.
P UNC WISHING EMPTY stilloutsidebag NOadditionalcharges. **Fdig2chargesTOTALUSED**
(engrave16589 + zF4T17256), leftunknown~2..6. zcreate6used,sfire5used,Astrike4used.
ONEHOLYWATEROstillbag, Qblessed+0GDSM+wrobe, reflectionI, Excalwielded,KOFF.
CircuitTAMElarge dogverified17344 stillALIVE15,20T17541. WraithNO LONGER inPK
17344; likelyCircuitkilled butNOseenmessage, donotassumedeathconfirmed.
3apes17307/10/43, waterelemental17418, quantum17456,troll17490,owlbear17495 allkilled.
PEACEFULGNOMEKINGUProom3,19T17541 LEAVE. AnotherG61,26SEnotlooked.
D16 **SWroom7..16,26..29 EMPTY**, **PIT13,26**, eastwallsearched10eachNOexit.
SWNdoor16,25->16,24->3..16,24->3,23->Sdoor3,22UProom. 3,22found1743x.
UProom3..23,18..21 Srow22 x3..23searched, ONLYknownS3,22, N6,17.
Ecentralcorridor fromW56,19->51..55,19->51,20->39..51,20
**SECRET46,20found17195**; **DUG34..38,20 from39,20 oneFcharge17256**
deadend34,20 NOTcomplete shortcutUProom24wall. DO NOTspendmoreFhere.
Corridor39,20S39,21/22->40..47,22->47,23..27->48..50,27->50,26
->51..59,26->**SE Wdoor60,26 unexplored NEXTtarget**. RoomSEG61,26(lastPK).
NoDOWNfoundyet. Northwest/northeast/UP/SW/Eroomsallknownexceptpossiblyhiddenexits.
GoldBAG3031. 3FOODcache67,18Eghostpile. LastOBS13:20:32healthy. LIVE noSTOP.

OLDER:
LATEST T17176 D16 ROGUE hero58,21 HP105 AC-12 XL10/9402 STR18/04.
**R3FOODRATIONS PACK**: ghost67,18pile5took2 +floor67,21took1; mergedBUCunknown.
**3FOODRATIONS CACHE67,18** withfakeamulet31arrowsbowmaceplatemail, leavearmor.
GhostKennethArnold67,18destroyed17118. GhostblankglyphonRoguefloor!
V CANDY EATEN17076. hONEjelly, Tcookie, qlizardunused. Lastfoodcandy17076.
GoldBAG3031 (+133UP,+105NE,+89E). Bag26stacks; P WISHINGEMPTYUNC nofurtheruses.
Allothergear unchanged: Qblessed+0GDSM MR, reflectionI,Excalwielded,KOFF,G OILLIT.
Circuitlastseen21,20T16980 thenfollowingafar, notseen17176, CHECKPKnext.
WraithfromD16luredD15T16963:1hit16964thenESCAPEDDOWN. ReturnedD16T16970
withCircuit, wraithlocationunknown. Don'twastechasing further.
D16MAP: UP10,20; **PIT9,19** avoid. UProom3..23,18..21, onlyNdoor6,17 known.
ScaleMAIL4,18LEFT. UProomN6,16->6..11,16->11,15->Sdoor11,14
->NWroom11..19,11..13 EMPTY. E20,13->21..26,13->W27,13
->Ncentralroom28..45,12..13 EMPTY. **SECRET46,13found1703x**
->47..56,13->**SECRET57,13found17058**->NEroom58..75,12..14 EMPTYgoldcleared.
**SECRET S68,15found1709x**->68,16->57..68,16->Ndoor57,17
->middleEroom57..74,18..21; ghostcache67,18, floorfood67,21cleared,gold69,20cleared.
MiddleE SROW22 searched n5s each2tilesfromx74to58 NOsecret; Wdoor56,19OPEN known,
headingwestnext. DOWNNOTFOUND. Owlbear9,26 earlierPKalivefarSW, wraithunknown.
GhoulUPdestroyed16924 afterfrozeCircuit(nowrecovered),snakeNW17003,
quantummechanicNE17061,koboldmummyE17115allgone nofoodcorpsesRogue.
LastOBS13:05:34healthy. LIVE KEEPPLAYING noSTOPmessage.

OLDER:
LATEST T16918 **D16 ROGUE LEVEL**, UP10,20 -> D15DOWN71,16. CircuitFOLLOWED11,20.
HP105/105 AC-12 XL10/9040 STR18/04. hONEroyaljelly remains: ate16909(+1STR),
lastfood16909, qlizardunused,Tcookie,Vcandy. P WISHING EMPTY outsidebag DO NOTWREST.
Q **BLESSED+0 GRAY DSM** verifiedaltar16850, WORNwithrobe; MAGICRES + REFLECTION.
P/F/J newwands **ALLUNCURSED** confirmedD15altar16843. Noadditionalchargesused.
Allpotions/scrolls BAGGED again16863, outero26stacks(mergedyellow), innerXbag4potions.
NewBUC: BLESSED MAPIROMAHAMADIROMAT scroll, BLESSEDemeraldpotion,
UNCskyblue, 2UNCyellow. ONEHOLYWATER O stillbag, nofurtherdips/prayers.
Circuitfreshgiantbatmeal16917. LastOBS12:55:15healthy. KEEPPLAYINGuntiluserstop.
D15DOWN71,16 room64..74,16..18, fountain68,17, grayoozeSTATUE73,18.
DOWNroomWdoor63,18->62..54,18->53,17->E52,17 potroom46..51,14..18.
**DARTTRAP49,17** found16811 harmlessmiss. DOWNroomW63,16openUNEXPLORED.
Sdoor69,19->69/68,20->68,21..24->68,25UP/ALTARroom. UProomUP73,28 ALTAR74,27.
D15NWroom6..11,13..17, E12,13unlockedopened16698 ->13..20,13
BOULDERnow21,13 bypass20,13SE21,14->21,18junction. E12,15->16,15->17,16DEAD
searched20noSECRET. E12,17deadendsearched20. S10,18->10..12,19->12,21->12,22SWroom.
Smallcentralroom25..27,23..25 N26,22->26/25,21->25,20->boulder25,19bypassnorth.
SmallroomE28,23->29..31,23 and E28,25->29,25->29..31,24loop.
31,23N31,22->31/32,21->32,20/19->33,19chestroom doorUNLOCKEDOPEN16800.
Mainrow24WEST33,24deadend notconnected to31,24 (gap32,24 stone).
D15 hostilesleft: floatingeyes59,24 later63,24 and32,20; giantbat51,22.
Wraithlosttrack(notinPK16908), do notassumedead. TinCircuitmovedto21,18 nowolditem.
D15gold64,17LEFT. OldHmithrilcache10,25; 4spareamulets chest36,16 unchanged.

OLDER:
LATEST T16687 D15 hero10,25 HP105/105 AC-12 XL10/9025 UNBURDENED.
**HUGE: P PINE WAND OF WISHING found10,25 T16678. First engrave wish granted
gray dragon scale mail Q. Requested blessed+2 but ACTUAL +0, BUCunknown!**
Q WORN with robe w over it; **MAGIC RESISTANCE NOW + worn I REFLECTION**.
H old+0 dwarvishmithrilcoat CACHED FLOOR10,25 D15. AC-12 vs old-9.
**zP16687 NOTHING HAPPENS => P EMPTY. DO NOT KEEP ZAPPING/WREST: destroyswand
and forfeits recharge! Need ID rechargecounter before charging (possiblebones).
No charging scroll identified yet. Preserve P, outsidebag. 1wishUSED.**
Wish armor enchantment+0 could RNG or luck; no confirmation lucknegative.
Graveyard23..26,13..16 CLEARED16639; chest24,14 unlockedtwicecheckedEMPTY.
HORNEDDEVIL25,13killed16627; wizardcorpse namedelron underneath, possiblebones
butnotconfirmed. Vampirebat26,13 becameVAMPIRE LORD destroyed16633. HPmin89.
WRAITH25,15 attacked2hits thenread ETAOIN SHRDLU TELEPORT16621, lastPK63,16
16660 ALIVE. Allzombiesgone. Nohero/petleveldrain. bdaggerRECOVERED16623.
CircuitTAMEalive lastgraveyard25,15, carryingTINfromcache36,16 to24,17.
G blessedOILlampLIT KOFF Excalwielded. Otherinventory/wandcountsunchanged.
D15westmap: CHESTROOM W33,16->32,16/17->29..31,17->29,18->27/28,18->27,19.
BOULDER26,19pushedWESTto25,19 T16609; bypassN25,18 orS25,20. S25,20/21 UNEXPLORED.
GraveyardSdoor24,17->24,18->24,19. W23/22/21,19->21,18junction
N21,17/16UNEXPLORED; W20/19,18->19/18,19->18/17,20->17,21..24
->SWroomEdoor16,24. SWroom9..15,23..25 EMPTYexceptHarmorcache10,25;
Ndoor12,22->12,21UNEXPLORED. Hero10,25 nextnorth. DOWNnotfoundyet.
LastOBS12:38:49 healthy. KEEPPLAYINGuntiluserSTOP.

OLDER:
LATEST T16601 D15 CHEST36,16 HP105/105 Pw16/16 AC-9 XL10/8361 STR18/03 UNBURDENED.
**CACHE CHEST36,16 D15** unlocked, twicecheckednotrap, nowcontains5items:
UNC concaveamulet, UNC pyramidalamulet, unknownBUC triangularamulet,
**UNC SPARE AMULETOFREFLECTION (Sokoprize)**, blackgem. ALL4spareamuletsNOWCACHEDnotbag.
**TINfloor36,16** left(noBUC/contentsknown), chesthasengraved"test"NOTElbereth.
WornIreflectionSTILLON, Excalwielded, GblessedOILlampLIT, KOFF, CircuitTAME37,17.
**NEW F WANDDIGGING** RUNED, 1engravechargeUSED16589, rest3..7 (verifygeneration),
**NEW J WANDCREATEMONSTER** unused FULLunknowncharges, unknownBUC.
Oldzcreate6chargesused, allotherwandcountsunchanged; NOnewfires/striking/poly.
NEW SKYBLUEpotion B picked51,15 BAGGED16567 unknownBUC.
NEW EMERALDpotionD,YELLOWpotionE chest36,16 BAGGED16589 unknownBUC.
NEW MAPIROMAHAMADIROMATscroll O picked35,18 BAGGED16597 unknownBUC.
NEW TRIANGULARamulet M picked36,18NOWCACHEDchest. Allpotions/scrollsbagged.
GoldBAG2704 (+40chest). O1HOLYWATERstillbag, labelsnotlettersstableafterreassignment.
F no longerfoodration, nowDIGGINGwand; h2jelly,qLIZARDunused,Tcookie,Vcandy.
Succubus36,17killed16581 HPbrief102now105. D15DOWNstillUNFOUND.
D15ALTAR74,27LAWFULbyUP73,28. UProom65..77,26..28 (Eedgeunexploredlastfewtiles).
Ndoors65,25opened16491,68,25alreadyopen,70,25opened16487; 70northbranchUNEXPLORED.
N65,24E->68,24->68,23UNEXPLORED; Wlongcorridorrow24x33..68,
SECRET58,24found16498and35,24found16522. WESTEND33,24searched15NOSECRET.
Row24junction51,24N->51,23/22->50,22/21->46,21/20->door46,19
->room46..51,14..18. Potion51,15cleared. E52,17UNEXPLORED;
W45,18open->44/43/42/41,18->41/40/39,17->SECRETdoor38,17found16571,OPEN16576
->CHESTROOM34..37,15..19. W33,16openUNEXPLORED(next),W33,19CLOSEDunopened.
Allotherroomitemscollected/cached, unknownchestgemleft. **NoIDscrollidentifiedyet**.
LastOBS12:10:09healthy, nextchecksoon. KEEPPLAYINGuntiluserstop.

OLDER:
LATEST T16482 **D15** HP105/105 Pw16/16 AC-9 XL10/8225 STR18/03.
**D15UP73,28 -> D14DOWN8,18**, **NATIVE TYR LAWFUL ALTAR74,27** rightbyUP!
Hero74,27 verifiedlawful; CircuitFOLLOWEDSTAIRS16481 tame73,28.
LastfoodF16147, h2jelly qlizardunused; noinventorychanges,WATER1BAG,GblessedOILlit,
ExcalWIELDED,KOFF,UwhistlePACK. Gold2664. zcreate6usedtotal; otherwandcountsunchanged.
D14completedknownroutes, secret52,12UNLOCKEDOPEN16366; waitedforCircuitD14DOWN
PONYattacked,killed16476, nocorpse. D14NEWcockatrice39,17 &demon41,17telepathy16453
LEFT; nointeraction, don'trunblindlythereonreturn. GnomelordUProomlast35,22left.
Nootherchanges. LastOBS12:10:09healthy, streamstillLIVE no cutoff.

OLDER:
LATEST T16365 D14 hero53,12 HP105/105 Pw16/16 AC-9 XL10/8205 STR18/03.
D14 ALLKNOWNROUTES explored; secret52,12found openingnow thenregroupCircuit->DOWN8,18D15.
**LAWFUL ALTAR24,17**, prayerSUCCESS16232; ROTHEoffered16237/FLOATINGEYE16240
bothHOPEFULcooldownreducedNOTcleared; doNOTpraysoon. ALLnewcorpsesfromaltarcleared/offered
exceptOLDwinterwolf25,18LEFT. Noaltarlootleft(otherthansling/helm23,17).
GblessedOILlampLIT aftermagicdjinniNOWISH16234; waREWIELDExcalverified16235.
HOLYWATER1 O BAGGED. GoldBAG2664(+64SEroom48,26). h2jelly,qLIZARDunused,FfoodEATEN16147.
Uwhistlerecovered16226. b/pPACK,pBURNT. KOFF. Allwandcountsunchanged,z6usedtotal.
**VAMPIREBAT wasSHAPESHIFTEDVAMPIRE**, chasedhero south, batkilled16321->VAMPIRE
trueform39,27 destroyed16324. NOLEVELDRAIN, Excalwielded; HPbrief95now105.
GECKO42,27 killed16288. RAVEN55,18killed16341corpseLEFTnow24turnsold(don'teatnext).
LURKERABOVE60,17 killed16347 corpseLEFTnow18turnsold. Oldtengu42,17/giantbeetle49,17OLD.
CircuitALIVEfollowingseen41,27T16324, subsequentautotraveloutpacedhim; NEEDlocatePK.
D14newroutes:40,20 SECRET40,21found16260 ->40,22->39,22doorOPEN UProom.
40,23->41/42/43/44/45,23->45,22->54,22->Ndoor54,23 SEroom48..56,24..28.
SEroomW47,27OPEN->40,27;40,27N->40,26/25/24/23(connectsup);
W39,27openUProom; S40,28/29->28,29BOULDER, bypass28,28DEADENDsearched15nosecret.
SEroomN56,23open->56,22/21/20/19->55,19/18->53,18->53,17maincorridor.
FARNORTH63,15->63,14/13/12->59,12 SECRET58,12found16359
->53,12 SECRETDOOR52,12found16365 opensintopriorSINKroom42..51,12..15.
Sink48,12untouched/yellowgem42,12LEFT. No shops. Boulders16,18 and28,29.
DOWN8,18 **BEARTRAP8,19**avoid. Statueyellowlight5,20, weapon8,19left.
LastOBS12:10:09healthyLIVEzeroerrors. NoteupdatedNOWISH. No cutoff; KEEPPLAYING.

OLDER:
LATEST T16234 D14 **TYR LAWFUL ALTAR24,17 CONVERTED16222** HP105/105 AC-9 XL10/7714.
**PRAYER SUCCESS16232**, made2holywater, +5maxHP; currentprayercooldownnewDO NOTpraysoon.
**G WASMAGICLAMP**, blessedvia#dipGO16232, #rubG16234djinni emerged
**"It is about time!" VANISHED NO WISH**. GnowBLESSED OIL LAMPLIT (limitedfuel).
RubWIELDEDG, NEXTCOMMANDwa(REWIELD EXCAL)then4tofreshrothecorpse23,17.
**O1HOLYWATER BAGGED**, CLEARcalledwater. NoMR/fire yet. No wishitemsobtained.
Circuit TAMEalive26,18, frosthitstwice16259? actually16158, survivedhealthyfollowing.
UwhistleSTOLENmonkey16217 recovered16226. KOFF. b/pPACK, pBURNTfromredmold.
FfoodrationEATEN16147, noFleft. h2jelly,qLIZARDunused,Tcookie,Vcandy.
zcreatewand **6totalchargesUSED** (1oldengrave,4firstsummons,1group16213).
Group: cockatricekilled16214nocorpse; freezingSphereexploded16215unaffectedcoldres;
succubuskilled16217, monkeykilled16217, homunculuskilled16218 CORPSESACRIFICED16222;
rothekilled16219 **CORPSE23,17 freshNOW**, floatingeyeblindkill16224 **CORPSE23,18freshNOW**.
RemainingVAMPIREBAT26,20 fleesfromaltar. DONOTeatOLDwinterwolfcorpse25,18.
Altarconversion: OWLBEAR27,17killed16066 hauled3stepsOVERTAXED thenoffered16089
FAILED (luck-1). Secondattemptwinterwolf k offered16210NOTHING age>50, dropped25,18.
Thirdhomunculus16222 SUCCESS(+1luck), nohostileminions. HeroLAWFULstill, godWELLPLEASED16232.
**MISTAKE16172 batchedfarlook+F4hitPEACEFULTENGU55,17**, angered. Disengagedbut
teleportedblockedpath42,17, KILLED16189. Userinformedbatchmistake. **NEVERBATCHunknownlook+Fattack**.
Tengucorpse42,17nowOLD; Circuitatethenleftvisiblecorpsemaybeunfinished. Giantbeetle49,17
killed1618xCORPSELEFT nowOLD. Fourwinterwolfcubskilled16152/58/61/62, coldreflectgood,
twofrosthitsCircuitwhilebeamMISSEDhero, petalive. Oldwolfcorpse65,16LEFT.
Secondowlbear66,16killed16138,CircuitATE. D14fullmapNOTDONE.
D14DOWN8,18 discovered, **BEARTRAP8,19 underweapon**, avoid.
Downroom5..11,17..22 NEopen12,17->13..15,17->15,18->16,19boulderbypass;
SEopen12,22->16,22->16,19loop. STATUEyellowlight5,20, weapon8,19LEFT.
AltarE27,17->longcorridor28..63,17. Junction40,17 N40,13->open41,13
->SINKroom42..51,12..15. SINK48,12, yellowgem42,12LEFT. Southdoor47,16->corridor47,17.
Junction40,17S40,20UNEXPLORED; corridorbranch53,18->55,18/19->56,19..21UNEXPLORED.
E63,17->63,16->63,15/14/13UNEXPLOREDN;63,15->66,15->NEroomdoor67,15.
NEroom68..73,15..19EMPTY, Wopen67,17->66,17/16central64/65/66,16loop.
NootherEexits. UProomE39,25/S40,26 STILLUNEXPLORED, closed39,22UNOPENED.
LastOBS11:58:12healthyLIVE0drops. Note currentlyoutdatedprewish; updateNOwish.

OLDER:
LATEST T16045 D14 hero16,19 HP100/100 Pw16/16 AC-9 XL10/6783 STR18/03.
D14UP38,23. **CHAOTIC ALTAR LOKI24,17**, NOpriest/mindseenexceptCircuit.
ALLbagitemsBUCcheckedby#tipo16020, recollectedandbagged. BagGOLD2600(+79D14UP34,27).
NEW2CURSED VERR YED HORREscrolls picked38,24 and35,27 BAGGED. NoIDyet.
NewBUC: UNC pyramidalamulet, murky/yellow/dark/golden/pink/invispotions;
PURPLE-REDpotionCURSED. TWOclearwatersUNC. NewVAS/JUYEDscrollsUNCmergedolderstacks.
**BAGLETTERSchanged** aftertip: n spareREFLECTION (formerlyC), C pyramidal,
R BLESSEDcloudy, O2UNCwater, Wdark, fWHITE, X ordinarysack4potions (repackedlast),
e2JUYED, g3VAS, v2cursedVERR, Bxor, Mzlorfik; labels/typesmoreimportantthanletters.
NOitemsleftonaltar. Heroallusualequipmentunchanged, allfragilesbagged.
**zCREATEMONSTERwand NOW5totalchargesused** (1oldengrave+4here16026..34),rest0..10.
Spawn1chickatrice killed16027 noCORPSE;2ironpiercer killed16030noCORPSE;
3REDMOLD killedranged16032noCORPSE; **pELVENDAGGERnowBURNT**, b/pRECOVERED16033.
4twoHILLORCS killed16035/36 noCORPSES. NOsacrifice/prayerattempted hereyet.
Orcishhelm25,17 andorcishdagger26,18LEFT. Circuit TAMEhealthy nearbylast26,20.
Nootherwandchanges, qlizardunused,h2jelly,F1ration; G LIT KOFF.
Altarroom21..26,17..20; Eopen27,19->29,19/20/21->31,21/22->32,22UProom;
Eopen27,17UNEXPLORED; Wopen20,18->19,18/19->18/17/16,19;
Wopen20,20->18,20->18,19samejunction. 16,19NBOULDER16,18bypass15,18;
16,19 SOUTHcorridor16,20..22unexplored. HeadingNW15,18.
UProom33..38,22..27 Eclosed39,22; Eopen39,25->40,25/26unexplored.
LastOBS11:33:03healthy. NOdeadline, continueuntiluserstop.

OLDER:
LATEST T15900 D13 UP58,15 HP100/100 Pw16/16 AC-9 XL10/6552 STR18/03.
Circuit TAME LARGE DOG56,15 caught up. KOFF, G LIT. GoingDOWN34,24 toD14unvisited.
D13 ALLknownrooms explored, NOaltar/shop. GoldBAG2521 (+25NE +43SE).
Noinventorychangesafter15739, allwandcountsunchanged, qlizardunused,h2jelly,F1ration.
DOWNroomEopen39,26->42,26->42,23->48,23->48,22->49,21/20->52,20UProom.
BUGBEARcorpse47,23 killed15752 OLD, dwarfmummywrapping47,14left15776.
SmallNroomEdoor48,12opened->49..53,12->53..57,13 SECRET58,13found15794
->59..66,13->NEroom68..75,13..15. Blacklight60,13exploded15797 halluCUREDax15798.
Giantbeetle62,13 killed15802, gnomemummy62,13killed15804 wrappingLEFT.
NEroomWopen67,15->66,15/16/17->65,17/18; Sopen69,16->69,18->70,18
->72,19->73,20->75,21->SEroomdoor75,22. SEroom71..75,23..27.
LONGWORM73,26 killed15836 CORPSELEFT nowOLD. PEACEFULDWARFLORDlast74,26donotattack.
SEroomW70,26->69,26/25/24->66,24->66,19->65,18centraljunction;
centralW64,18->63,18->63,13 loopsnorth; nootherroomsfound.
ANTIMAGIC30,14avoid. Allotherknownlivinghostilescleared; mindlesspossible.
LastOBS11:24:52 healthyLIVE zeroerrors. No cutoff. Connectionincidentresolved.

OLDER:
LATEST T15739 D13 hero34,24 DOWNSTAIRS HP100/100 Pw16/16 AC-9 XL10/6198 STR18/03.
CircuitTAMEdog30,24 following. F1foodrationPACK NEWbarrowwightloot15631,
h2jelly,qLIZARDunused. Pancakefloor8,21 EATEN15709 noillness. b/pPACKbothrecovered15625.
BagGOLD2453 (=2279+16UProom+53smallNroom+105SWroom). Noothergoldpickup.
NEWscrollJUYEDAWKYACC e picked31,14unknownBUC BAGGED15626;
NEWscrollVASCORPBETMANI g picked29,17unknownBUC BAGGED15632.
Floatingeye31,14 killedblindfolded15622; KOFF15623. Barrowwight29,17 killed15630.
ANTI-MAGICTRAP30,14 drainedPw5 nootherdamage,avoid. Fountain32,15untouched.
D13UP58,15 DOWN34,24. Noaltar/shopsofar. EASTBRANCHESstillUNEXPLORED.
UProom53..61,15..20 WEST52,15->52,14->49,14->open48,14->Nsmallroom42..47,12..14.
NsmallroomEclosed48,12UNOPENED; Wopen41,12->40/39/38,12->37,13->35,14
->door33,14opened->fountainroom28..32,13..15; Sopen28,16->28..32,17
->32,20->33,20->open33,21->DOWNroom26..38,22..26.
DOWNroomEopen39,26 UNEXPLORED(next); Wopen25,23->23,23/22/21->21,21..13
->open20,13->NWroom14..19,13..16EMPTY; Wdoor13,16opened->11,16..25
->SWroomdoor10,25->smallSWroom7..9,21..26EMPTYnowgold+pancakecollected.
UProomwest52,20alsoUNEXPLORED. SWroomnootherexit. NeedfinishEbeforeD14.
LastOBS11:11:46 healthyLIVE, noDeadline. Reconnectincidentfullyresolved.

OLDER:
LATEST T15595 MAIN D13 UP58,15 HP100/100 AC-9 XL10/6099 STR18/03,unburdened.
Circuit TAME LARGE DOG successfullyFOLLOWEDSTAIRS fromD12 at15595, now59,17.
D13 initialdrop15496 fromD12TRAPDOOR32,14; killedsoldierant56,19 T15498.
D13UP58,15 ->D12DOWN50,13. ReturnedD12forCircuit15503, nowbothD13.
D13UProomknown53..61,15..20, WESTdoors52,15 and52,20closed; gold60,17collectingnow.
D12circuittookmaze43,19,telepathy15528 located,tameconfirmed. Rejoined45,25T15546.
NewD12SHORTCUTS: N61,15->61,16->61,17->65,17->65,19->65,21->67,21
->67,23->65,23->65,25->Sstrip. CENTRAL45,25->45,21->41,21->41,15->Nstrip.
Centralbranch41,17->43,17->43,19->41,19 (Circuitlocation) explored.
D12horse51,13killed15570 CORPSELEFT; Circuitateworm35,12 andkilledpeacefulgnomelord
~15573 (petkillnothero), loots34,12and35,13. Circuitfetchedlongswordto48,13LEFT.
D12VIOLETFUNGUS last51,16; LARGE MIMIC? boulder57,11 revealedmtelepathyNOTFORMALLYID.
SleepingNYMPH71,12 andLONGWORM73,12 left; peacefuldwarfkingwest,blacknagaS.
YELLOWpotionEbagged15473; MURKYpotiond picked37,13 T15475 BAGGED15476.
Copperspellbook45,14 LEFTunread. NOothernewinventory. WATER2 inbag; noholywater.
ZpickaxeCACHED18,27 D12. BhighbootsCACHED27,28 D12. LbuckledbootsWORN AC-9.
b/pPACK; bready. G LIT. Allwandcountsunchanged, qlizardunused,h2jelly.
LastOBS10:59:20 healthyLIVE aftersuccessfulSSHreconnect; NOdeadline/userstop.

OLDER:
CONNECTION INCIDENT RESOLVED ~05:40UTC Sept7: hide, SSHescape newline~., start,
loginwithprotectedcredentials, `r`ResumeLastSave ->RESTORED SAME T15474 HP100.
Free `:` responded. StreamSHOWNagain, noteconnectionrestored. No gamequit/newgame,
no admincontactneeded. Separate spectator exec59818 CLOSED(exit0). Rootcausenotknown.
Floor37,13 MURKYpotion + longsword; pickingonlymurkymenu b now. Verifyletter.

OLDER:
URGENT T15474 REMOTE GAME UNRESPONSIVE (2026-09-07 ~05:33..05:38UTC).
Hero37,13 D12 HP100/100 XL10/6011 AC-9; noadjhostile, manes35,16 distant.
Lastworkingbatch aosE66, baggedYELLOWpotion E thenmoved35,13->37,13.
Potion37,13 notyetpicked (comma/:/Escape/C-r/C-q/C-c allnoresponse).
SSH alive; Hardfoughtlobbyseparateconnectionresponsive. SPECTATORshowsSAMEfrozenframe.
Noerror/crash/deathmessage. DoNOTdestroyoldgame/startnew. TrysafeSSHreconnect;
ifstalegame/adminrequired followhttps://www.hardfought.org/nethack/ crashrecovery.
OBSlast10:47:57 healthy; streamLIVE. Publicnote connectioncheck.
Separate spectatorterminal execsession59818 watchingourgame (read-only); closeafterdiagnosis.
D12DOWN50,13 discovered15446. EntireouterstripN y11..14 andW x5..7 clearsmaze.
MAGICTRAP5,11 triggeredharmlessshiver15446,avoidnow. PEACEFULdwarfking12,14,
PEACEFULgnomelord33,11 last15474. 1stLONGWORM35,12 killed15470 CORPSELEFT.
2ndLONGWORM73,12 tail74/75,12 75,13 73,11; nymph71,12 asleepunknownspecies.
YELLOWpotion E picked35,13 BAGGED15473. Potion37,13 unknownstillfloor.
Spellbook45,14 uncollected. Weapon43,13 unknown; gems31,13/10,12left.
Zpickaxe CACHED18,27 confirmed15426. BhighbootsCACHED27,28. DsecondwaterBAGGED.
CircuitlargeDoglast65,28beforeleavingSvision15442; maystilldistractedbycorpses.
ALLwandcounts unchanged; b/pPACK,bready. G LIT. Noailments,unburdened.

OLDER:
LATEST T15425 D12 BigRoom hero18,27 HP94/100 XL10/5816 STR18/03.
BOOTSWAP15417: L blessed+0buckledboots NOWWORN; B+0highboots CACHED27,28.
AC now-9. Pyramidalamulet C picked27,28 BAGGED15417 unknownBUC.
SecondCLEARWATER D picked18,27 T15424, baggingnow. Priorclearwater n alsoinbag.
Zpickaxe REMOVEDfrombag15425, CACHING18,27 now tosolveburden. Verifycommands.
Outerbaglikelyoilskin; weightremaining tight. Gold2279 unchanged.
b/p BOTH PACK recovered58,26 T15387 afterjellyfight. bready.
OCHREJELLY killed15385 afterengulf15382 (HP94->80), no wandused. G relit15386.
Circuit largeDogalivefarSE62,29 stilldistractedbycorpses; killedquiveringblob15381
andhumanzombieearlier. Nojelly/blobSEleft. NewACIDBLOB26,28 avoidmelee.
2manes killed15354/15405, MOREmanes24,25 and30,28. PEACEFULblacknaga wandering.
Tool35,26 isMIRRORleft. D12DOWNstillunknown, entire northernmazemostlyunexplored.
LastOBS10:40:56 active0drops/congestion/reconnect. Continueuntiluserstop.

OLDER:
LATEST T15327 MAIN D12 BIGROOM hero58,26 HP76/100 AC-10 XL10/5700 STR18/03.
Circuit TAME large dog last63,25. b/p recovered15296/15301 then BOTH THROWN WEST
at third soldier ant15326/27: b floor52,26; p floor53,26; ant54,26 wounded.
Bag2279gold (62centaurgoldcollected15303). No foodrationsPACK, h2jelly, qlizard.
Additional kills: adultcockatrice65,25 T15300 NOcorpse; dwarfzombie63,26 T15318;
ironpiercer57,26 T15323. Chickatricecorpse69,26 nowOLD; nevereat/touchbarehanded.
Hostiles: soldierant54,26, quiveringblob67,25, MANES21,26; peacefulblacknaga26,26.
D12 northernmaze: 65,25->65,23->67,23->67,21->65,21->65,19->65,17.
OCHREJELLY63,17 blocks westcorridor; avoid fornow. ReturnedtoopenSstrip.
Alternative northopenings57,24 and53,24 unexplored. DOWNstillunknown.
Lootuncollected: tool35,26, amulet27,28,potion18,27. 2rations67,25cached.
Allwandcounts unchanged (fire5used). LastOBS10:33:29 healthyLIVE.

OLDER:
LATEST T15292 MAIN D12 BIGROOM hero64,25 HP65/100 AC-10 XL10/5480 STR18/03.
NewPET **Circuit TAME LARGE DOG**, tamedtF4 at15247, named#name m15247.
Circuit65,26 EATINGhorsecorpse15290; previouslyatecentaur15256..15289. Noobservedpetdamage.
NOFfoodrationsPACK (lastFusedtame). h2royaljellyPACK,lastateeh15285 healed9+STR18/03.
**b/pdaggersOUT**: thrownwest15266/67 againsthorse. b+0pickedGreyelfthenTHROWN
atme15270 missed, landedunknownlikely66,26. pUNCelvendaggerlanded61,26 maybeinelfloot.
NeedRECOVERboth; inspectpiles63,25/26 elfloot,61/65/66,26missiles. DoNOTassumeb/pPACK!
Bag2217gold(+101goldgolem64,25), purple-redpotionvcollected68,26thenBAGGED15253unknownBUC.
NewtotalFIREs5chargesused (fifthzs1hitEttinmummy15285), remaining0..3.
A STRIKING4used unchanged,Ypoly1used,tunknown2used. NootherwanduseinBigRoom.
**D12UP70,27** ->D11DOWN33,13. **D12DOWNNOTFOUND**. Onlysouthstripmapped sofar.
**CHICKATRICECORPSE69,26LEFT killed15236**, keepglovesu andExcal, qlizardPACK.
BigRoomCLEAREDnearSE: chickatrice15236,dustvortex15239,koboldmummy15241,
yellowlight15254,mountaincentaur15256,horse15270,3Greyelves15274/75/80,
goldgolem15278,2soldierants15282/84,Ettinmummy15286,chameleon15289,2giantrats15286/90.
XL10firstGreyelf15274 MAXHP88->100. LowestHP57ants, jellyheal66, now65regen.
PEACEFUL BLACKNAGA wanderingfarW last23..27,26/28, DON'TATTACK.
Remainingknownhostiles QUIVERINGBLOB72,26slow; IRONPIERCER54,27; i(impclass)last10,26
nowoutofsightunidentified. RestBigRoomunexplored. Noimmediateadjhostiles15292.
Loot: centaur2FOODRATIONS+roundshield+missiles67,25 (Circuitleftaftermeal).
Elfloot63,25 and63,26 weapons/armor/foodneedinspect. Mummycorpse63,27rottedDONOTEAT.
Koboldwrapping71,27. FarWamulet27,28,potion18,27,tool35,26uncollected.
LastOBS10:16:53healthyLIVE, continueuntiluserstop. Updatebeforecontextloss.
D11LEFT15235. Portalunfound. NewFfungus41,14downroom, smallNW23,15searchednosecret.

OLDER:
LATEST T15184 MAIN D11 hero49,14 deadend searched15 nosecretfound.
HP88/88 AC-10 STR18/02 Wi10 XL9/4698 normalburden,notsatiatedsince15038.
PUCE=calledCONFUSION from49,26 pickedn15017, hornDIPxn15018->CLEARWATER
unknownBUC, BAGGED15019. FIRSTWATERowned readyforaltarblessing.
Bag2116gold (D10:2059 +D11:11+7+21+3+15). Bagnow22stacks.
b/pdaggersPACK(pready). Jaguar52,20killed15032, corpseOLDsoon. Nocurrenthostiles.
F1UNCfoodration,h3royaljellyPACK, RcramcachedD10; lastmealroyaljelly14873.
D11DOWN33,13. UP51,27, MAGICTRAP52,27AVOID. QuestportalNOTLOCATED.
FoodrationsLEFT51,24UProom and39,24centralSroom. ScalemailLEFT36,15downroom.
D11UProomN52,23->52,19->door52,18->Nroom51..56,13..17 EMPTY, ONLYknownexitS.
UPwest48,25->47/46/45,25->44,24->43,23->42,22->door41,22
->centralSroom32..40,21..26. SEdoor41,26UNLOCKED/OPEN15156 loops43,25.
CentralS N40,20->40,17->door40,16->DOWNroom31..43,12..15.
DownroomW30,12->29,12/13->25,13->door23,13->smallNWroom18..22,13..15.
SmallNWwest17,13/17,15->corridor13..16,13..18->doors11,15/11,18
->FARWESTroom3..10,15..20EMPTY goldcollected. SmallNWeast23,15UNEXPLORED.
Corridorbranch43,21->44,20 TIGHTSQUEEZE: DUG43,20T15164 withZpick.
waREWIELDEDExcalandZREPACKED15166. ->44,19->47,19->48,18..15->49,14DEADEND.
Boulder47,18unmoved. SidebranchsmallNW23,15 stillfrontier. BroadfarEblanknotaccessibleyet.
LastOBS10:01:05healthyLIVE. Continueuntiluserstop.

OLDER:
LATEST T15015 NEW MAIN D11 UP51,27, QUESTPORTALfloor (Nornmessage), XL9notquestready.
HP88/88 AC-10 STR18/02 Wi10 XL9/4658 SATIATED noailments normalburden.
MAGICTRAP52,27AVOID. Fountain51,26. Gold52,25; potion49,26; food51,24.
Entryroom48..53,24..27 northOPEN52,23 westOPEN48,25.
LastOBS09:55:00healthyLIVE. Continueuntiluserstop.
D10 DOWN23,13->D11UP51,27; room21..29,12..17; gold73at28,17bagged.
Bag2059gold after+73downroom+127SWroom. Fogcloud36,12killed14958.
Wi10exercise14904. Allwandsunchanged, F1UNCfood+h3jellyPACK.
D10downroomwest20,15->19,17->17,19->15,20..23->OPENdoor14,23
->SWroom4..13,23..26 EMPTY(gold10,26collected). SecretCLOSEDdoor9,27UNOPENED.
SWeast14,26->17,26..29->26,29->26,25hiveEloop.
D10downroomE30,12->38,12..15; E30,15->38,15connectionmapped15014.
Centralroom42..45,14..17 WESTopen41,14and41,16, NORTHsecretCLOSED44,13,
EASTopen46,14and46,17. FoodrationLEFT42,15.
CentralE46,14->48,14->50,13->50,12->53,12->OPEN54,12UProom.
Otherbranchesmostlyloops, noaltar/shopfound. NE/UProomremainingcloseddoorsunopened.

OLDER:
LATEST T14891 MAIN D10 hero26,19 northsecretCLOSEDdoor26,18 openingnext.
HP88/88 MAX+1, STR18/02, XL9/4631 AC-10 SATIATED, unburdened.
HIVEcleared14870 queen+11?bees, meleeonly, bdaggerrecoveredPACK.
Royaljellyeaten14865/73 raisedSTR18->18/01->18/02 andMAXHP87->88.
FirstjellyrottenBLINDcuredhorn14871, noailmentsnow. h3royaljellyPACKunknownBUC.
Fnow1UNCfoodrationPACK; cached1UNCfoodration22,25hive and1UNCfoodration+Rcram25,25.
Darkpotionj+GOLDENpotionk frombeedrops25,25 bothunknownBUC BAGGED14883.
Bag1859gold after109at41,26. Bagnow21stacks. OBS09:48:51healthyLIVE.
D10southcorridor70,28west->57,28->57,26->43,26->door42,26 DARKroom33..41,23..26.
Darkroomwestopen32,23UNEXPLORED; westopen32,25->31,25SECRET30,25found14838
->26,25->hiveEdoor25,25. Hive21..24,24..27, northOPEN21,23 ->21,22->24,21
->25,20->26,19->secretCLOSEDdoor26,18found14891. Nocurrentadjhostiles.
Eastroomh66,24seenwhileblind unknownpossiblypeacefuldwarf; farlookfirst.
Horse70,28killed14798 corpseOLD; invisibilityworeoff14812.
DO NOT EAT whileSATIATED. ContinueexploringD10; DOWNstillnotfound.

OLDER:
LATEST T14796 MAIN D10 hero71,27 HP87/87, hostileHORSE70,28 attacking.
TemporaryINVISIBLE fromquaffUNC O SWIRLY14777 => formallyINVISIBILITY.
SparefSWIRLYunknownBUCfound69,14 BAGGED14775; oldOconsumed. Normalburden.
Heroabsent@whileinvisible: terminalcursorstillcorrect. F3foodPACK,lastmeal14761.
Bag1750gold after73NEroom+67SEroom. LastOBS09:34:28healthy.
D10northdoor61,21OPEN ->61,20->63,19->67,19->67,17NEroom66..69,14..16.
TRAPDOOR68,20AVOID. NEroomwestCLOSED65,16;westOPEN65,14unexplored;
east70,15->72,15->72,27verticalcorridor. SEroomentrance73,27 room74..75,27..28
emptygoldcollected. Westbranch71/70,27->69,28->68,28 UNEXPLORED.
Nextresolvehorse70,28 thenexplorewest. Downstairsnotfound.

OLDER:
LATEST T14761 MAIN D10hero64,23 HP87/87 XL9/4110 AC-10 SATIATED aftereF.
Foodrationeaten14761, Fnow3UNCfoodrationsPACK. Unburdenedaftermeal.
WATERN YMPHkilled14747at61,23. Noitemsstolen. ASTRIKINGwand used2zapsbyhero
14745/46,plus2orc=>4TOTALknownchargesused, remaining0..4. sfirestill4used.
NymphPINKpotioncollectedletterbthenBAGGEDo14752, likelyobjectdetectionbutNOTID.
MirrorLEFT61,23. b+0daggerwasallocateddthen#adjustdb restoredBOTHb/pPACK.
MainD10UP59,13 room55..59,12..14. WESTclosed54,12,EASTclosed60,14,
WESTopen54,14unexplored; SOUTHopen57,15->57,16/17->59,17..20->59,21roomentry.
Southroom59..68,22..26 EMPTYbesidesnymph; CLOSEDnorthdoor61,21next.
Hero64,23 nexttravel61,22 thenopenNdoor61,21. Nootherknownenemies.
Bag1610gold. Allscrolls/potionsinsideo, Lblessedbuckledboots/AstrikingPACK.
OBS09:29:45healthyzero skips. LIVEcontinueuntiluserstop.

OLDER:
LATEST T14735 MAIN D9 DOWN28,28 ->NEWmainD10. HP87/87 AC-10 XL9/4085.
MainD9UP48,17,DOWN28,28. Fiveemptyrooms,55gold70,18collectedbagged,bag1610.
Routes:UProom46..59,16..19 WESTdoor45,16->43,16/17->40,18..21->38,21->
38,23..25->33,25/26->31,26hidden30,26->secretopen29,26->downroom21..28,26..28.
DownroomNdoor24,25->23,24/23->21,22..20->19,20..16->door19,15->
Nroom19..31,13/14 EMPTY. Westexit18,14->17,14/15/16->13,16->12,17->10,18..25
->door9,25westroom4..8,21..26 EMPTY. DINGO killed14635 no corpse,Rcramrecovered.
EastUPexit60,18->61,18/17->67,17door68,17unlocked->eastroom69..73,17..20.
EastroomSW68,20->65,20->61,20/21->48,21->46,22->41,22 loopscentraljunction.
Loosebranches41,25deadend and33,28southunsearched; likelyloopsdownroom29,28east.
MINETOWNwatchstillHOSTILE nohero guardkills, gearBUCdone, safelywithdrew.
LastOBS09:25:51healthyzeroskips. Continueuntiluserstop.

OLDER:
LATEST T14578 MAIN D8DOWN36,14 proceedingNEWmainD9. HP87/87 AC-10 XL9/4045.
SuccessfullyWITHDREWMINETOWNwithoutkillingwatch. Allwatchhostileafteraccidental
strike14427. Neverbatchforceattacksnearpeacefuls again. MinetownUP77,17exit14465.
Mines1werejackal drankSMOKYpotion14509=>GAINLEVEL observed; noneowned.
Werejackal39,18last14511, u38,18UNKNOWN couldMercury (don'tattackwithoutlook).
Allvaluablelootrecovered. mCURSEDemerald, othernewringsUNC. Potionsallrebagged.
G lampUNC, xhornUNC, pdaggerUNC. L BLESSED+0buckledbootsPACK,AUNCstrikingPACK.
F4UNCfoodrationsPACK (verifycount), packgold0 bag1555. No newintrinsicafterSLEEP.
LastOBS09:16:26healthyzero skips/reconnect/congestion. Continueuntiluserstop.

OLDER:
LATEST T14432 MINETOWN ALTAR47,21 HP80/87 XL9/3974 AC-10. RETREATING!
WATCHNOWHOSTILE:14427F6F6 killedrockmolefirst,peacefulwatchmansteppedintosecond
forceattack! Ownbatchingmistake acknowledgeduser. DON'TBATCHATTACKSnearPEACEFULS.
NoWATCHKILLEDbyhero yet. Watchman48,21 spear,chasing. Captainalsohostile.
PlanWITHDRAWnorthdoor48,18 ->mainMinesUP77,17. ALLLOOTRECOVEREDexceptcursedblank
leftaltar47,21. NOholywater/prayerperformed. Lastprayer10627still.
AltarBUC: mCURSEDemerald; i/SUNCshiny/wire; xhorn/Gnewlamp/sfire/tcrystal/Ypoly/
pdaggerALLUNC. yconcave,Csparereflection,AstrikingALLUNC. LBLESSED+0buckledboots.
McloudyBLESSED, OswirlyUNC, WwhiteUNC. PLOREMearthBLESSED,QLOREMearthUNC.
EKO BATE/vXOR OTA/jSTRCPRSTSKRZKRK allUNC; g2VASUNCmerged; DVENZARstillCURSED.
Bagotipped14412, Xordinarysack4potions,Zpickaxe retrievedthenREPACKEDo.
INSIDEo now Xsack,Zpick,Cspare,P/Qearth,DcursedVENZAR,nZLORFIK,JHACKEM,
eJUYED,g2VAS,yconcave,1555gold,Mcloudy,O swirly,Wwhite,EKO,vXOR,jSTRC.
LbootsPACK,AstrikingPACK,F4UNCfoodrationsPACK(probably4check),allringsPACK.
GHOSTKaytempleevent14399fright3turns, destroyed14402 (+159XP). RopeGOLEMhit14400
flednorthnotkilled. Blacklight?HALLU14422 duringrepack,curedax14423.
MercuryMines1Dl5nowPEACEFULNOTTAMEfireant25,15T14339. Leavealone.
Soko1spares38,18/39,18bothcheckedempty now38,19/39,19. Wandstillmissing.
OBS09:05:47healthyzero skips; LIVEcontinueuntiluserstop.

OLDER:
LATEST T14218 Soko2aDl4DOWN30,16 returningSoko1. HP87/87 AC-10 XL9/3763.
UNBURDENED afterdropping1UNCfoodration44,25Soko2a; Fnow1rationPACK,
W3rationsINSIDEo. b/pdaggersBOTHrecoveredPACK. WERERATkilled14188at45,25,
corpsegone2CRAMleft. WOODLANDELFescapedearliernowKILLED14198at43,25lootleft.
Top4a imp33,15killed14152. Topcache45,25alsoCURSED ridingbootsf nowdropped.
TopPRIZEspareREFLECTIONCinsideo; NOBOH. ReturnMinetownaltar.
NeedcheckSoko1spareboulders38,18/39,18 forguaranteedwandifmovable.
OBS08:57:32healthy. Usernostop yet, continue.

OLDER:
LATEST T14112+ SokobanPRIZEcollected14099 C AMULETOFREFLECTION (spare,insideo).
Hero45,25 top4a, HP77/87 XL9/3684 AC-10 Dx17. AllpuzzlesDONE.
PRATYAVAYAH=>SCAREMONSTER guaranteedcursedscroll LEFT43,28 withburntElbereth.
NewDWHITEpotion45,26 andE KO BATEscroll45,25 bothcollectedINSIDEo.
y concaveamulet/Astrikingwand/Csparereflection/W3foodrationsINSIDEo.
b/pdaggersBOTHRECOVEREDPACK. RedN mealROTTEN14086blind curedax14087,
unfinishedcorpse49,26. Auto-reviewBLOCKEDresumingmeal; don'tretrywithoutapproval.
NoFIREresgain. ExtraGartersnakekilled14088. Gnomeking+tenguPEACEFUL.
CACHING45,25 oldeggJ, 3UNCblankL+3unknownblankZ, oldBLESSEDalmostemptyOILlampd.
Oneblankstillinsidebag. PlanreturnMinetownaltar forBUCandID; floor4ringmissing.
OBS08:53:16healthy0skips. Continueplayinguntiluserstop.

OLDER:
LATEST T14084 TOP4a hero49,26 HP70/87 XL9/3682 AC-10, BURDENED afterloot.
ALLFOURPUZZLESSOLVED. Zoo cleared except leprechaun46,27; gnomeking andtengu
are CONFIRMED PEACEFUL, DO NOT ATTACK. Chickatrice killed14059 NOcorpse seen,
q lizard unused. Trollcorpse FULLY EATEN14081 at50,26; no revival threat.
Now eatingREDNAGA corpse49,26 killed14052, fresh32turns. Fireintrinsicnotyetknown.
p elvendaggerRECOVEREDpack; bdaggerFLOOR47,26. x unicornhornPACK new14053.
y CONCAVEAMULETunknown new14084 PACK; A STRIKINGwandnew14084PACK,
orcused2zaps. 1514goldjustbagged, total1555goldINSIDEo, pack$0.
PrizeNOTCOLLECTED:43,24/26 closetsopenapparentlyempty;44,28doorCLOSED.
Likelyprize43,28; noattackwhileonburntElbereth. Floor4ringstillunfound.
Loot45,25scroll45,26potion;49,26orcarmorcorpses; bdagger47,26underorcgear.
sfire4chargesused, tcrystalnoeffect2chargesused, vXOROTAinsideo.
LastOBS08:49:03 healthyzero skips/congestion/reconnect. Continueuntiluserstop.

OLDER:
LATEST T14053 TOP4a ZOOFIGHT hero50,26 ONDOOR HP69/87 XL9/3291 AC-10.
ALLPUZZLESSOLVED, door50,26OPEN14023, triggeredzoo14029, fightoutside51,26
mostly. Now50,26 toreachloot. x UNICORNHORN recovered14053 PACK!
bUNC+0daggerRECOVEREDfromtroll14053 PACK; pELVENdagger stillFLOOR49,26.
TROLLCORPSE UNDERHERO50,26 killed14049; NOTdisposed. FIRE DOESNOTBURNIT!
Incorrectearlierassumptioncorrected; farsawtrollcorpseafterzap14050.
NeedEATonceadjacentenemiescleared orrevivekillagain. Corpsepile50,26includes
blackunicorn14036,owlbear14039,goldenN14041,rothe14047,troll14049. Nofootriceyet.
Blackunicorn,succubus14046,redN14052,scorpion14032,soldierant14049,quasit14043,
wintercub14050,owlbear,goldenN,rothe,trollKILLED. Someothermonstersnaga killed.
RemainingCHICKATRICE46,26approaching; qlizardcorpsePACKforgradualstoning.
At14053adj IGUANA49,26,MORDORORC49,27, Z49,25; manyorcsrow24,tengu,gnome,Bat,
yellowlight44,24(prizeroom43,24empty?),leprechaun46,29, q48,23. Doors44,24/26
openedBYMONSTERS;44,28stillclosed. PrizeNOTcollectedyet, ringfloor4notfound.
sFIREnow4chargesused TOTAL (engrave1,blocker1,zoo2); unknownremaining0..4.
t CRYSTALwandfoundunderQ36,25T13985,PACKcallednoengravingeffect. Engrave1charge
13987normaldustNOeffect; zaplockeddoor50,26NOeffect14021 ->NOTopening unlessempty.
2chargesused likelylocking/probing/undeadturning/nothing. KEEPoutofbagunknown.
v XOR OTA scrollfromGreyelf34,20stashedINSIDEo13996. Noothernewpackfragiles.
Ospare31,25 Qspare35,25, bothcheckedoriginals. Ring4notfoundmaybezoo.
Foodcache35,18slimemold29,25ration; elfloot34,20foodration,armor,cursedelvendagger.
LastmealGreyelf13793confirmedSLEEPres. Newwestimp35,19telepathy14026maycomebehind.
OBS08:31:11healthy0skips. Stilllivecontinueuntiluserstop.

OLDER:
LATEST T13953 TOP4a ALL16HOLESSOLVED13950! ALLFOURPUZZLESSOLVED.
Hero51,14 HP87/87 XL9/2730 AC-10. pELVENdaggerRECOVERED51,14PACK.
OnlyO30,25 Q36,25bouldersremain. CheckingO r next, Q l after tolookunder.
No hiddenholesremain. LastenemyYETI13897killed34,16 corpseOLD13953DONOTeat.
Theninspect34,20GREYELFLOOTscroll? plusmithril,CURSEDelvendaggeramongweapons.
NeedZOO next door50,26 via51,14..26. All3prizeclosets44,24/26/28closed.
LastknownzooCHICKATRICE45,23 SUCCUBUS47,29 TROLL46,28 manyothers.
qLIZARDCORPSEpack,sFIRE2chargesused,Ypoly1used. Sleepresconfirmed13793.
OBS08:16:27healthy0skips. No deadlineuntiluserstop; keepplayinglive.

OLDER:
LATEST T13816 TOP4a hero47,14 HP87/87 XL9/2677 AC-10 Wi9 STR18. 14/16FILLED!
SLEEP RESISTANCE CONFIRMED13793 'You feel wide awake' eatingfreshGreyelf34,20.
4Greyelveskilled13768/70/73/79at34,20. FirstelfCURSEDelvendaggerwelded,
laterelfpickedmithril. LOOT34,20 HAS SCROLL? visibleaftercorpseeaten, inspectlater.
Remaining A30,18 andE38,18 required, O30,25 Q36,25spares. B/Dgone.
NEXT A r*5 ddd lll ddd uuuu rrr uuu l uuu r*15=>49,14HIDDEN;
thenE lll ddd lll ddd uuuu rrr uuu l uuu r*16=>50,14, OMIT hidden49whenfilled.
pELVENdaggerFLOOR51,14recoveroncecorridorcomplete. hburied45,14; bPACK.
Lastmeal13793Greyelf; OWL13427. No activewesthostileknown. ZooSEALED.

OLDER:
LATEST T13690 TOP4a hero33,28 HP79/79 AC-10 XL8/2509. 12/16FILLED.
P/Jgone, hdaggerBURIED45,14. Only49,14hiddennow. Remainingholes47..50,14.
Dnow34,27, executing uuuu ll uuu rrr uuu l uuu r*13 =>47,14.
ThenB32,18 rrr ddd lll ddd uuuu rrr uuu l uuu r*14=>48,14.
A30,18 r*5 ddd lll ddd uuuu rrr uuu l uuu r*15=>49,14.
E38,18 lll ddd lll ddd uuuu rrr uuu l uuu r*16=>50,14.
O30,25 Q36,25spares checkunderforring/wand. Floor4ring/wandnotfoundyet.
Imp13587killed34,16 corpseoldnow. Urukhai13593killed36,20(10HPdamagehealed),
invisibleUrukhai13595killed36,21 usingPKtelepathy; RKdone13596.
RAT51,14KILLED13651bythrownpELVENdagger, pNOWFLOOR51,14safeafterallholes.
bdaggerPACK, hburiedlost. Fire2chargesused. qlizardcorpsePACK. Lastmeal13427.
OBS08:10:04healthy0skips. No activewesthostilesknown, zooSEALED.

OLDER:
LATEST T13526 TOP4a hero34,17 HP79/79 XL8/2441. 10/16FILLEDthrough44,14.
Rgone. P31,27currentlyexecutingrrruuuulluuurrruuuluuurrrrrrrrrrr->45,14.
HIDDENHOLES NOW45,14underhdagger AND49,14underfood. PassBOTHuntil45filled,
thenomit45. hdaggerwillbury, fine. b/pdaggersRECOVERED38,14T13520PACK.
Mindlessunseenblocker38,14killed13511 withsFIREONEzap+p/bdaggers; hthrown
AFTERkillwastedlandingonhole45,14. sFIREnow2chargesusedtotalinclengrave.
BlindfoldPK13508sawno blocker; zooallstillsealed, rgiant rat51,25then51,14.
Zombie13471killed. Lastfoodowlbear13427. NoHPdamage. OBS08:00:19lastcheck.

OLDER:
LATEST T13456 TOP4a hero42,14 HP79/79 AC-10 XL8/2355 Wi9. 9/16FILLED.
H/G/F/I/C/K/L/M/Ngone. Remainingholes44..50,14; ONLY49,14hidden.
Owlbearkilled13403, ateFRESH29,24finished13427, notSatiated, rationsunused.
NEXT R33,27 r+uuuu+ll+uuu+rrr+uuu+l+uuu+r*10 ->44,14 (runningguard).
ThenP31,27 rrr+sameuuuu...+r*11, J29,27 r*5+sameuuuu...+r*12.
D33,25 needsrdddlllllurrrrruuuu...r*13; B/A/Eneedroom3loopseeWiki4a.
O30,25 Q36,25sparescheckunderlater; floor4wand/ringstillunfound.
OBS08:00:19healthy0skips. ZooSEALED. qlizardcorpsePACK,sfirewandPACK.

OLDER:
LATEST T13287 TOP4a hero39,14 HP79/79 AC-10 XL8/2273 Wi9 (exercise).
6/16FILLED H/G/F/I/C/Kgone. Remainholes41..50,14 (49,14hidden).
L33,23 next luuurrruuuluuurrrrrrr ->41,14. M35,23 N37,24 R33,27
P31,27 J29,27 D33,25 B32,18 A30,18 E38,18 thenO/Qspares.
Gecko13166 andfox13275killednoHPdamage. GIANT RATseen51,14acrossholes13246,
notvisible13287; don't confusewithrockmole. OBS07:54:38healthy.

OLDER:
LATEST T13113 TOP4a Dlvl2 hero34,14 HP79/79 AC-10 XL8/2267. SETUPALLDONE.
HfilledFIRSThole35,14. Onlyhiddenhole49,14 now: use --hidden-hole 49,14.
NextG31,20 rrrruuuluuurr->36,14; F29,20 rrrrrruuuluuurrr->37,14;
I38,20 llluuuluuurrrr->38,14. C32,24 D33,25 J29,27 K30,23 L33,23
M35,23 N37,24 P31,27 R33,27. A30,18 B32,18 E38,18 O30,25 Q36,25.
Ponykilled12978, corpsesoldDONOTeat. Lastmealspinach12775 nohungry13113.
OBS07:50:30healthy0skips. ZOOsealed, noothersactive. Continueuntiluserstop.

OLDER:
LATEST T12961 SOKO4a TOPFLOOR Dlvl2 ENTER12932. Hero36,24 HP79/79 AC-10
XL8/2247 Str18 $41. 0/16holesfilled, HIDDENholes35,14 AND49,14 under%food.
ALLplanner calls use --hidden-hole 35,14 --hidden-hole 49,14 untilrespectivehole
filled; omitconsumedonesafterward. Addedargtoplanner guardsknownhiddenholes,
routesavoidthem andcorrectlyexpectsboulderconsumption. Compilepassed.
DOWN28,14 ->Soko3UP46,21. NoUPontop. Longholecorridor35..50,14 toeast51,14
then51,15..26, door50,26→zoo45..49,23..29. Prizeclosetsdoors44,24/26/28.
ZOOstillSEALED. Telepathy12936 CHICKATRICE45,23, SUCCUBUS47,29; manyorcs,
ants,Snakes,Nagas,Troll46,28, othercritters. Noattackthroughdoorsyet.
2GIANTMIMICSinitialwest:35,17mimickingboulder killed12944,29,23mimickingfloor
killed12957. HP79nosuccessfulhits. CorpsesDONOTeat(usemakesimmobilemimic).
Originaltopfloorboulders A30,18 B32,18 C34,18 D36,18 E38,18 F31,20 G33,20
H36,20 I38,20 J31,21 K31,23 L33,23 M35,23 N34,24 O30,25 P32,25 Q36,25 R30,27.
SETUPDONE K l=>30,23 andN rrr=>37,24. Runningguard session71511 R30,27rrr
=>33,27. PollthenNEXT P32,25 rrdddllllur =>31,27; F31,20 ll=>29,20;
J31,21 rddddrrdddlllllu=>29,27; G33,20 ll=>31,20; H36,20 ll=>34,20;
D36,18 ldddlllddddr=>33,25; C34,18 rdddlllddd=>32,24.
THENholefilling H34,20 ruuuluuur =>hole35,14 (hidden), G31,20 rrrruuuluuurr
=>36,14; F29,20 rrrrrruuuluuurrr=>37,14; I38,20 llluuuluuurrrr=>38,14.
Furtherplansfrom https://nethackwiki.com/wiki/Sokoban_Level_4a readFULL.
Validateeveryplanandguardmax50. Othercurrentfood35,18SLIMEMOLD,29,25unknown;
2foodstacks35,14/49,14onholeswillbury ifboulderfill, okayplentyfood.
CURRENTs FIREWAND (glass) PACK engravetest12920 ONEchargeused, burntElbereth
onSoko3 48,20. q LIZARDCORPSE PACK picked12915 (nonrottingpetrificationcure!).
I CONFIRMEDuncursedamuletREFLECTION worn. G lampLIT, dlowOFF, Ypoly1chargeused.
ALLSCROLLS NOWINSIDEo after12929: e/g/j/k/n/J/D/P/Q/f/Z. Oldlettersreused
onfuturepickups! IncludesbothEARTHP/Q,4newblanksf/Z,alloldunknownpricedscrolls.
M CLOUDYpotionalsostashedINSIDEo12908; ohas~19itemsinclnestedordinarysackoldm.
m EMERALDring PACK, iSHINYring PACK,S WIREringPACK,r BLESSEDopalPACK.
b/h/p daggersallRECOVERED12883, pELVEN. No darts. W3+F2foodration,Rcram,Tcookie,Vcandy.
Soko3FOODcache48,19ration and43,24unknown left. Alloriginalboulderfloor3checked.
Soko3spares A37,17 D38,17 E39,18 B34,18 J40,19. No bouldersbroken.
Soko2escapedWOODLANDelfnearUP47,19 remains futurethreat. PetsstillMinetown/mines1.
OBS07:28:06healthy0skips; check~5min. No deadlineuntiluserstop.

OLDER:
LATEST T12855 SOKO3a SOLVEDALL11holes! LastCfilledhiddenhole48,26, foodfellin.
Hero47,26 HP79/79 AC-10 XL8/1869 $41 Str18 (SPINACH tin12775raised17->18).
I octagonalamulet NOWFORMALLYIDENTIFIED AMULETofREFLECTION! Cubfrost12813
reflectedfrommedallion. WORNuncursed. Hugeupgradeinourknowledge.
YwandPOLYMORPH PACK1chargeused. G lampLIT, dlowfuelOFF. NoMRknown.
Floor3guardsimproved autoDISMISSexactread-only 'Things that are here:' popup
ifcursorheader andexpectedhero@, excludespickupquestions. Thenallchecksrepeat.
Testedpassedarmorpopup128xx. Otherprompts/monsters/boardsstillsafestop.
Newm EMERALDring from37,21, BUCunknownPACK (oldmordinarysacknestedINSIDEo,
letterreused). pELVENdagger pickeddownstair37,26thenTHROWNcub; recovered12820.
b+0daggeralsorecovered12820. hsecondUNCdaggerTHROWNcub12816 MISSED, remains
somewherefartherEtoproom(probably39,17), recoverwhilecheckingtoproomspares.
Wand3NOTFOUNDyet; inspectunder B35,18,D38,18,E39,18 allUNMOVEDoriginals.
CURRENTactionguarded session73026 B35,18 l=>34,18 toinspectunder. Bcannotu
(35,19WALL). ThenD38,18 u andE39,18 u exposefloors. A37,17 andJ40,19already
movedfromoriginals, noitemsseenunderoriginals. Acurrentblockscenterroomentry,
canwalkvia36,16->37,16->38,16. No needdestroyANYboulders. Guardmax50.
Enemies: WoodlandelfESCAPEDDOWNstairsT12749 ->Soko2UP47,19 expecthostilethere.
2otherwoodlandelvesKILLED12752/12755, neitherleftcorpse: secondTINspinachate
12775, St18Satiatedbrieflynowordinary. Loot37,23 elvenmithril+jungleboots left;
36,26 elvenleatherhelm+elvenshieldleft; spear40,26left. Oldcavespider35,22corpse.
WinterwolfCUB12819killed (triggeredreflectionID); python12839killedcorpse37,26
freshuntil~12880 butno needfood, spinachlast. Eggs32,19rottedaway.
UPROOMunopened door49,25, UP46,21. Telepathy12833 showedlizard:44,19 andS43,22,
noothervisible living. Beware mindless nottelepathy. FullHPcontinueup4thafterloot.
OBSlast07:20:05healthy0skips. PreviewvisuallyverifiedcolorAIlabel~07:14.

OLDER:
LATEST T12615 SOKO3a Dlvl3 hero41,26 HP79/79 AC-10 XL8/1692. ENTER12529.
5/11holesFILLED, remaining43..48,26; LAST48,26HIDDENunder%food, parsercounts5
visiblebut6real! DoNOTwalk48,26untilboulderfilled. Planninglastboulderwillthink
notconsumed; expectedboardmismatchsafeafterfill unlessrevealedearlier.
Runningguard session74229 G34,19 dddrddddrrrrrrrr =>6thhole43,26. Pollinspect.
Originalbouldercoords A35,17 B35,18 C36,18 D38,18 E39,18 F33,19 G34,19
H36,20 I37,21 J40,21 K34,22 L35,22 M38,22 N37,24 O36,25 P36,26.
K/L/N/O/P NOWCONSUMED; othersunmovedexceptGbeingpushed.
AfterG: F33,19 rdddrddddrrrrrrrrr =>7th44,26.
M38,22 rrlllllddddrrrrrrrrrr =>8th45,26 (rrfirstneededstandright).
J40,21 uu=>40,19 thenI37,21 dddddrrrrrrrrr =>9th46,26.
H36,20 rddddddrrrrrrrrrr =>10th47,26.
A35,17 rr=>37,17, thenC36,18 ddrddddddrrrrrrrrrrr =>last48,26.
VALIDATEwithplanner each; monitorpopups/monsters. Mayneedchunkmax50.
DOWN37,26 toSoko2UP47,19. UP46,21 eastroom door49,25locked.
Food32,19 and48,26 stillfloor, otherlootunseenunderboulders. G lampLIT.
Fullsol https://nethackwiki.com/wiki/Sokoban_Level_3a read. OBS07:10:17healthy.

OLDER:
LATEST T12483 SOKO2a SOLVED12369 ALL12holesfilled, heroUP47,19 HP70/79 AC-10
XL8/1692 $41. Currently n45s restsent tohealthenUP3rd floor. No activehostiles;
WHITEUNICORNpeaceful49,16, moldF45,17 notapproach. Door51,24OPEN.
Killedspider12376, guardianhatchling12381, REDNAGA12382, giantbat12386,
GELCUBE12392, LYNX12395, quiveringblob12409. HPmin52 healed. AteREDNAGA
12400..12436 interruptedblob resumed; NOFIREresmessage. Earlierdingo12348
ate12356. Newg VAS CORP BET MANIscrollunknownBUC fromrednaga50,23 picked12437;
g noLONGERdarts bothdartsdestroyedthrowingcube. b/hdaggersrecovered12396.
Y ALUMINUMwand engravetest12370 POLYMORPH calledpolymorph via #name oY.
1chargeused, safeOUTbag currently. Newi SHINYRING picked28,20T12459;
S WIREringfromfloor1 unchangedbothuntested. rblessedopalringold.
GnewLAMP LIT12335; dBLESSEDoillampOFFnearlyempty(abouttogout12333).
Xoldalmostemptylamp and Oduplicatetinwhistle DROPPED51,24T12398.
ExtraCLOUDYpotionalso51,24 LEFT declinedburden; McloudyoriginalstillPACK.
GelcubeCORPSE51,24 andgiantbat50,23OLD no eat. 2cram29,21left.
Guarded scripts/sokoban.py nowMAX50steps accepted, default20, allperstepchecks
unchanged: cursor/hero/boards/HPvsPREVIOUSsnapshot(notinitial)/conditions/monsters.
FLOOR2 sparedA29,18 D29,19 B33,19immobile F36,19; C/Gconsumedlasttwo.
OBSlast07:02:27healthy0skips/reconnect/congestion. No stopdeadline.

OLDER:
LATEST T12116 SOKO2a hero36,24 HP79/79 AC-10 XL8/1387 $41. Guardedexecution
running session8654: H37,24 push drrrrrrrrrr tohole47,25 (9th), expecthero46,25.
8holesfilledNOW, 4remain47..50,25. Guard stoppeditempopup12089correctly;
paperGolem12062killed then4blanks picked12091 => Z3unlabeled+f1unlabeled PACK,
BUCunknown. ORIGINALfCURSEDbootsstillINSIDEo, lettersreused! Newgolemguard
includes apostrophe andhuman@, notjustalphabetic. ALWAYSuse --execute guarded.
CURRENTspares A29,18 UNMOVED, D29,19 movedup1, B33,19 IMMOBILE accidental.
F36,19 unmovedspare. Working E32,20(movedright1); G30,21(movedright1);
C35,19 replacementforB; H37,24currentlyfinishing; I/J/K/L/M/N/O/P consumed.
NEWPLANafterH9th: E32,20 push drrdddddrruurdrrrrrrrrrrr =>10thhole48,25.
Then C35,19 dllldrrdddddrruurdrrrrrrrrrrrr =>11thhole49,25 (checkplanner!),
then G30,21 rrrrdddddrruurdrrrrrrrrrrrrr =>12thhole50,25.
A didNOTmoveup duepopup guardstopped; likelynoneedmoveitforCaccessvia28,18.
Ifplannerblocked, inspect route ratherthanblindpush. TwoimmobilizedsparesOK.
2CRAMrations29,21 LEFT becauseburdenwarning declined12097. SHINYRING28,20
stillfloor. Ape33,21corpseoldDONOTeat; lastfreshape11971alreadyeaten. dLAMPLIT.
YaluminumwanduntestedPACK. S wire ringuntestedPACK. O/UbothTINwhistles.
Noactivehostiles12116. OBSlast6h30m04healthy; checkagainsoon. No deadline.

OLDER:
CRITICAL UPDATE T11993: anotherAPE interruptedbatch11984, B boulder33,20
accidentallypushedUP33,19 NOWIMMOVABLEcorner. Stillenoughbouldersbutcannot
useBperwiki; replaceBwithC35,19later (canpushd,l,d-route). ApeKILLED11984,
HP76/79XL8/1370. Icurrently33,23 needs rdddrruurdrrrrrrrr to7thhole45,25.
scripts/sokoban.py NOW supports GUARDED --execute --max-steps20(default20max25)
checkshero,cursor,boulders,holes,HP,conditions,visiblemonsters afterEVERYSTEP,
stopsimmediatelyifunexpected. 0.45secstep20~10sec. Readonlydefaultstill.
Useguardedpushingfromnow; avoids rawlongbatcheslosttoappearingmonsters!
Test10steps11984..11993passed. Currentlyguardednext20running session64275;
pollcompletiontheninspectactualboardandreplanremainingpushesfromcurrentcoord.
PlanI totalfrom11993 rdddrruurdrrrrrrrr, resultinghero44,25 5holesremain.

OLDER:
LATEST T11971 SOKO FLOOR2a Dlvl4, hero42,25 HP79/79 Pw12 AC-10 XL8/1344 $41.
FLOOR1a SOLVED11683. EXPERTlongsword11687, XL8mummykill11708. Foodcollected:
Tcookie,Vcandy,W3rations total (1floor1+2floor2, messageW2pickup means added),
F2UNC rations,Rcram. Atefreshape11958..11971, nohungry/satiated. Needfullinvverify.
Y NEW ALUMINUMWAND floor2at36,21 picked11772 UNTESTED, keepOUTbaguntilID.
Soko2a 6/12holesfilled; remaining45..50,25. Hero42,25 afterapemeal. FIRSTnext
I boulder33,22 push drdddrruurdrrrrrrrr ->7thhole45,25. Currentactionbatch22keys
executing; inspectactualbeforecontinuing. functionsstore soko_remainingholdsrest
butreadactualboard toconfirmnohostiles first. Fullplannedsequencebeforefirst22:
444444844888426222448868622242662688244886644888866262224266666666
Soko2a originalletters map: A29,18 B35,18 C36,19 D29,20 E31,20 F36,20
G29,21 H32,21 I33,22 J30,23 K34,23 L32,24 M37,24 N34,25 O37,25 P30,26.
CURRENTremaining A29,18 B33,20 C35,19 D29,20 E31,20 F36,19 G29,21 H32,21
I33,22(movingnext) J30,23; K/L/M/N/O/P consumed. No boulderbreaks/cheating.
AfterI finish: J rrrrdddr ruur drrrrrrrrr (derive/check exact viawiki/planner).
Then A u; G r; D u; E r. Then B/E/H/Ginto4remainingholes. Wiki2a solution
https://nethackwiki.com/wiki/Sokoban_Level_2a readverified. Readagainasneeded.
Soko2a DOWN30,16 UP47,19 behinddoor51,24. SHINYRING28,20stillfloor! Collectlater.
Soldierantcorpse37,25oldDONOTeat, ape42,25eaten. Noactivehostiles11971.
OBS6h30m04healthy0skips. No deadlineuntiluserstop.

OLDER:
LATEST T11684 SOKOBAN FIRST FLOOR1a SOLVED11683, hero34,17 belowUP34,16
hostilecentipede34,16. HP69/69 AC-10 XL7/1254 $41. No boulders broken/luckpenalty.
DOWN36,16 toMAIN D6 SOKOUP49,27 FOUND11400. All10pitsfilled2spares38,18/39,18.
Foodstillfloor42,19cookie,44,18candybar,45,19foodration. CollectbeforeUP.
P and Q scrollLOREM IPSUM guaranteedEARTH from34/35,24, BUCunknown,
R CRAMration collected34,23 with S WIREringunknown. F2UNCfoodrationspack.
M CLOUDYpotionNEWmainD6Sokoroom49,28, ONEWwhistleT11403 testedhigh=>TIN,
oldUalsoTIN. NoMAGICWHISTLEyet. dBLESSEDoilLAMPLIT; XOFFnearlyempty;Gunknownlamp.
L newBUCKLEDboots bought89Malasgirt mainD6shop72,26, +0 NONCURSED removeOK.
No speedmessage, #jump cannotjump=>LIKELYWATERWALKING boots. INSIDEo now.
BhighbootsbackWORN AC-10. Hmithril+0 WORN, wrobe+0 WORN. v/EarmorSOLD.
o now7items: m4potions/nogold,fCURSEDboots,tUNCpick,LNEWboots,qswirly,
3blankscrolls(originalLletterinside),egg. Beware letters reassigned on takeout!
Mercury LEFTMINES1Dlvl5 lasttamechameleon27,23T11227; EmberMinetownstore29,25.
Lastprayer10627. IntrinsicsSpeed/telepathy/coldres/poisonres; sleepmemorized10718.
MainD6 hiddenrouteSOLVED bydigE63,23->64,23->65,23->66,23, connects65..68,24
->MalasgirtARMORshopdoor69,24, floor70..74,24..26. Allpaid. Onlybootsworthbuy.
Fromcorridor65,24 SW64,25->61,25->61,26->60,27->60..51,28->door50,28
room47..49,27..28 SOKOUP49,27. Westdoor46,28unknownoutsideoldpiercers.
FloatEye49,28killedblind11401; bugbearshop11387; gecko11477/bat11608 killed.
scripts/sokoban.py NEWREADONLYplanner X Y pushesr/l/u/d -> keys+expectedhero.
UsescurrentterminalBFS cardinalwalk avoids0/^/monsters, NEVERsendskeys.
Callescalatedprefixpython3 scripts/sokoban.py. Validateactualafterbatch,
monsters/Thingshereautopopup can interruptmovement! Splitlongroutes~20keys.
Floor1a solutionhttps://nethackwiki.com/wiki/Sokoban_Level_1a verified;
twoearthP/Qcollected, wireS+cramR. OBS6h20m37healthy0skips, no deadline.

OLDER:
LATEST T11313 Main D6 upstairs22,20, HP69/69 AC-10 XL7/1200 $130allpack.
H NEW DWARVISHMITHRILCOAT bought320mainD4shop11260, WORN11270, enchant0
BUCunknown (no coldcursefeedback). wrobe actually+0 NOT+1; worn. vLEATHERsold3.
E cursedELVENcoat SOLD120atSiverek67,16. Allpaid. Old Ocloak/sleepx/velvety sold.
dBLESSEDoilLAMP nowPACK LIT11121. X nearlyemptylampOFF11124. GunknownlampPACK.
mordinarysacknow4POTIONS NO GOLD, inside o. tPICK beingtakenoutnow11313.
o othercontents fCURSEDboots,qUNCswirly,L3blanks,egg. F2UNCfoodrationspack.
Mercury T11227 tameCHAMELEON27,23 MINES1Dlvl5 leftbehind after~80turnswait,
aliveconfirmedtelepathy. EmberMinetown29..31,25storeleftwellfed. Bothrecoverlater.
APEcorpse eaten11227..11244 satisfied/satiated, now satiationgone11301.
Little dog11111,jaguar11126,koboldzombie11160,ape11225 killed. Lastprayer10627.
Sleep a learned10718, failure likelyhigherwithmithril now (was41%leather).
MAIN D4 newPIT31,12 besideDOWN33,12, avoid. Shopmimics71,16/17.
NEXT mainD6 southeastdeadend63,23 digtowardunknownarea; avoiddamagingshopwalls
(Malasgirt70,25 telepathyold); Sokobanmustonthislevel. Shopwallswarnhardtodig.
OBS6h00m06healthy0skips. No deadlineuntiluserstop.

OLDER:
LATEST T11011 Minetown UP77,17 HP69/69 AC-6 XL7/1149 $243+84 inside m inside o.
Mercury adjacent76,17 Uruk-hai, finished owlbear meal. Ascending NOW to mainD4
armor shop: mithril coat72,17 cost320; total327. Ember tame large cat left
Abitibi store31,25 after prolonged unsuccessful coaxing; well fed, recover later.
Pick t UNCursed after prayer10627, INSIDE o bag. wUNC+1robe WORN. Ocloak sold.
x sleepbook read10718 then SOLD50; spell a sleep level1, 41%failure. yvelvet
book SOLD113, level3 unknown. D cursed VENZAR scroll base100, do NOT blindread.
F2UNCfoodrations bought/paid12010767 and altarchecked10776. E CURSED elven
mithril coat found free deli10760, altarchecked10776, now INSIDE o, sell or uncurse.
G NEWunknown lamp found10784 at43,19 Minetown, pack BUC/price unknown.
X oldoil lamp LIT11002, littlefuel; dBLESSEDoil lamp unused INSIDE o.
o contains m(84gold+4potions),t pick,E cursed coat,f cursed boots,d lamp,q potion,
L3blankscrolls,originalegg. Bag unknown BOH/oilskin, never mix cancellation.
Tyr priest DEAD10602 Mercury; altar works but no sanctuary. Temple topdoor48,18
NOW OPEN/unlocked, west44,20 and SW44,22 open. Lastprayer10627, antclover10624.
Mercury shapechanges rapidly, sometimes invisible in darkness even to infra;
oil lamp reveals. Killed watchman10950, loot70,15 left. Don't personally attack.
All shops paid. Stream5h53m36 healthy0skips. No deadline; continueuntiluserstop.
NEXT ascendMinesD6up73,25 -> D5up39,15 -> mainD4shop; then mainD6 pick-dig
hidden Malasgirt shop70,25 and Sokoban upstairs. MainD6up22,20 down10,13.

OLDER:
LATEST T10654 Minetown altar47,21 HP40/69 AC-6 XL7/866 $138+84INm.
PICKAXE t UNCursed by THIRDprayer10627; aExcaliburWIELDrestored10628.
Prayers8286/9548acceptedbutfailedminorfix, 10627successafterantSACRIFICE10624
clover=>Luck+1, cooldownwas0. Lastprayer10627 now. NO godangerknown.
CRITICAL: recruitedSHAPESHIFTER10495 withWfruitwhilewarhorse. NAMEDMERCURY10651,
currentlypaperGOLEM45,21. Changesrapidly, SAMEnamepersists. Tame confirmed.
Mercury killedTyrpriest10602 whileminotaur; TEMPLE NO LONGER SANCTUARY.
Altarstilllawful47,21. Topdoor48,18 LOCKED(byuskeyl); westwall44,20 and
southwest44,22 nowOPEN due rockmole. East49,21wasdugthenmerchantrepaired.
Newcat tamed10633 bythrownwolfcorpse, NAMED EMBER10654, last45,22. Original
missingpetsstillunresolved; possiblethiscatwasferaloriginal, cannotknow.
NEW wUNCURSED+1ROBE WORN=>AC-6; O+0cloakpack. xUNCURSEDlightgreenSPELLBOOK,
yUNCURSEDvelvetSPELLBOOK, unread, maybe sellforfood. DNEWCURSEDVENZAR BORGAVVE
scroll obtained10644, altarcheckedretrieved10651, basepriceUNTESTED.
oBAG nowcontains mORDINARYsack(84gold+4potions), fCURSEDboots,dBLESSoilLamp,
qUNCswirlypotion,L3blanks, original1EGG. UnknownBOH/OILSKIN, safecontainer.
XoldoilLAMP flickered8364 OFF8365. No foodremainingexceptEGGinbag! AteV8715,
Y9477/Y10148,Q10600; WfruittamedMercury. CurrentlynotHungry butneedBUYFOOD.
Combatcleanup: severalwolves,zombie,rothe,quiveringblob,violetfungus,rockmole,
gridbugkilled. ImmediateHOSTILEjaguar46,21, hero47,21, sent44nexttofinish.
Mercury/Emberhelping. HP40safeishrestneeded. GofoodshopandpriceD/books; then
UPmainD6Sokoban hiddenroutepick. Restinventoryunchanged. Stream5h33m42healthy.

OLDER:
LATEST T8248 Minetown Dlvl7 hero26,21 heading altar47,21 for cursed PICKAXE.
HP69/69 AC-4 XL7/680 intrinsicSPEED7850, poison/coldres/telepathy. $112 +84INm.
Lastprayer6900, staffedTyrtemple. Plan wieldcursedpick thenprayuncurse; Excalibur
temporarilyunavailableuntilcured. No identifiedRC/holywater. Food3rations+lembas+fruit.
PETS MISSING: catlast63,21D9T7974, horse68,24D9T8108. No deathmessage. Neither
ontelepathyD9/D8/D7; catalsoabsentD10. Suspectunseenlevelteletrap eastD9corridor
63,21->UP54,24, unconfirmed. Do NOT assumealivepresentor dead. Checkupperlevels.
AllD9stashRETRIEVED8110. mordinarysack holds84gold+4potions(oldrGOLDEN/y/A/S).
qNEWswirlypotionUNCURSED base150. kVASscrollUNCURSED base200. i mergedL3blanks.
dBLESSEDOILlamp base10offer4, #rub3nothing re-wieldeda8208; XoldlampLIT7211.
oUNCURSEDBAG containing1egg base100(offer43incl egg)=>BOH/OILSKIN, nottricks.
fCURSEDridingboots base30=>LEVITATION/FUMBLING, do NOT wearuncured.
rNEWBLESSEDopalring base150, worn8247 noobservableeffect removed8248.
hUNCURSEDdagger; b+0daggerquivered; lKEY. Restinventoryunchangedbelow.
Alloffersdeclined+retrieved; nodebt. Merchant28,24, test30,25 notentrysquare.
D9UP54,24 DOWN71,26, pinch68,25->69,26 requiresweight<=600, horsecannotcross.
D10UP38,13 DOWN52,16 peacefulTENGU46,17 bypassbelow. D11UP38,22 DOWN48,20.
D12UP22,19 DOWNunfound. RandomminesnotEnd. 4manescleared8038. LEVELTELETRAP
southwestbranchnear2..6,25..28 senttoD10T8085. Mosteast/northD12unexplored.
OBS5h17m07healthy. No time limit. Continueuntiluserstop. Cursorlineaddedharness
compact output: terminalcursor usuallyherocoordinates (distinguishpriests/guards).

OLDER:
LATEST T7956 Mines5 Dlvl9 hero55,12 exploringnorth. HP69/69 AC-4 XL7/672.
LEVEL7 gained7850 orcshamankill; intrinsicSPEED. Monkeykilled7916. Poisonres.
New lKEY7814, oUNKNOWNBAG7854 containing1egg(nootheritems; NOTbagtricks),
kVAS CORP BET MANIscroll7785, iunlabeledblank7744, qswirlypotion7946.
AllnewBUCunknown. f ridingboots,dsecondlamp stillunknown. b/hdaggersrecovered.
FoodV1/Y2rations,Qlembas,Wfruit; ateV7870. $112pack84INmordinarybag.
Mines5 UP54,24. Southloop54,24->47,27->44,25->46,22->48,20->54,20.
Mainhighway40..63,19. Antimagic45,19; spikedpits47,28&31,19.
Westconnection40,18->39,17/16->37,16->36,14->32,13->32,17->30,19
->28,20->centralwestcave16..30,20..22. SOUTHpocket26,29 DEADEND.
Eastspurcentral32,24->36,25DEADEND gnomealive.
Westcave9..16,20..27 connects7,27 ->2..6,27..29DEADEND. NWvia10,19
->9,18 ->3,17 ->3,15DEADEND. Dwarfstilldiggingfarwest4,18T7885.
TIGHTunexplorednorthopening18,18->17,17 blockedcarryingweight, likelysmall
14..17,16pocket. _@x. oftenkeepsaimingatthisblockedfrontier, choosemanualfarther.
Eastmainhighway63,19->65,18->65,16->64,15->62,14->60,13->55,12.
UpperNEcave49..61,12..14 CURRENTexploring. MostotherNEunknown.
SEmain60,22->61,25pocketseen butnotwalked,65,23unexplored furtherSE.
Gnomelord66,17petkilled7949 bowleft, gem67,15left. Bothpetsalive.
OBS4h52m41healthyactive. Do NOT stop untiluser. No deadline.

OLDER:
LATEST T7635 Mines4 Dlvl8 hero21,15, heading DOWN8,25 FOUND7617!
HP60/60 AC-4 XL6/622. Killed leprechaun7616, got112gp;84gpINSIDEbag.
New f unknown riding boots picked14,23 (BUCunknown, do NOT wear untilchecked),
h unknowndagger picked21,16. Weapon21,15/27,14 bows,22,14aklys, no pickfound.
Westnewroutecentral17,21 ->17,22 ->14,23 ->10,23 ->9,24 ->8,25DOWN.
Bothpetsalive largecat/warhorse following. XlampLIT. dsecondunknownlamp.
Eastfullyscouted: giantcave52..65,18..22 loopsvia68,26 southhighway48..68,26;
farSE75,28deadend. Antimagic63,18 discovered7522; beartrap65,17,36,25.
Wand38,17 seen7571 vanishedbeforearrival7578 (likelypet/gnomepicked).
Native _@x. travelnearestunexplored VERY useful; _@>. travelsknownDOWN.
OBS4h37m33 healthy active zero skips. No time limit. Continueplaying.

OLDER:
LATEST T7426 Mines4 Dlvl8 hero70,14, HP57/60 AC-4 XL6/588 $84, allwell.
Iuncursedoctagonalamulet WORN7181, noidentifiedeffect. Xoil lampLIT7211.
dNEW unknownlamp picked42,13 at7373 (BUC/identityunknown). Vnow2foodrations
(extraMines4free36,17 picked7226), Y2foodrations,Qlembas,Wfruit. Poisonres7056.
Housecat grewLARGE CAT by7363; bothpetsalivewithhero7426. Horsefreedbeartrap
36,25 (approxnotyet^mapped). HERObeartrap65,17 at7409 escaped7421, leghealed7423.
Antimagictrap18,13 at7299. Yellowmold50,13 killed7384 darts/knife; recovered
b+0dagger and1dart, nowg2darts total (threw3lost2). bquiveredcurrently.
Mines4 UP31,28 ->33,27->33,26->34,25..20->35,20->36,19..17->37,16..14
->38,13 -> NORTH HIGHWAY38..52,13 ->52,14/15 ->58,15->59,16->61,16
->61,17/18/19 EASTERNCAVE floor58..65,18..21. Trap65,17 leadsNEemptyroom
67..70,12..15 deadend. CURRENT headingback64,21 toexploresouthx63,22unmapped.
Mines4 DOWNnotfound. EastfarG74,26 suggestsfurthercavern.
Westmap: northerncorridor13..52,13 antimagic18,13; NWroom11..28,12..19,
centralfloor18..36,19..25; southwest dugloop16..24,25..30 deadend except
connection21,26->21,25->22,24->central. Lowboots22,26left; gems20,29/17,30.
Dwarf23,28 foughtcat7290 thenvanishedtelepathy by7308; no loot24,28/24,30.
Otherh20,17alsoGONE7329 aftercatwent21,16. Maybecatkilleddwarfnorthlater,
potentiallootUNSEENaround20,16..18! Check onreturn, notalreadysearchedthere.
Eastern spur36,18->40,18->41,19->42,19->43,20->44,20..24 DEADEND.
Yellowlight37,24 alive stationarynotyetexploded, avoid. OBS4h23m32healthy.

OLDER:
LATEST T7153 Minetown downstairs11,13 waitingpets. HP60 XL6/584 AC-4 $84.
POISON RESISTANCE acquired T7056 from black naga hatchling corpse (acid11HP,
healed). Confirmed "You feel healthy." Blacknaga20%chance won. Thirdape fled
to9,15; twootherskilled7103..7106. Catlasttown26,25 beforelongtravel, alive
hopefullyfollowing. Warhorse12,14adjacent alive. Generalstore exited, bothpets
eventuallyOUTSIDE7062; nofightmerchant. AllpurchasesPAID7018, no debt.
FoodV1/Y2ration,Qlembas,Wfruit. Xlampunused. Prayerlast6900, poison/cold/telepathy.

OLDER:
LATEST T7018 Minetown Abitibi GENERALSTORE southwest entrance27,24, floor28..31,
24..26. Hero28,25 exitingnext. HP60 AC-4 XL6/525 $84. FoodrationT ate7014,
nowV1ration,Y2rations (PAID7018), Qlembas,Wslimemold. NhelmCONFIRMED+1.
Sold qordinaryharp19gp, EEMPTYstriking75gp, COrcishspear2gp,lCURSEDspeed100gp.
X oil-lamp boughtIzchak13gp (not lit yet). Izchakdoor41,24, floor37..40,24..26,
mimic39,24 AVOID. Allcandlesexceptlamp37,26 whichwepurchased. No magiclamp.
PRICE-ID offers at Abitibi (declined/retrievedall exceptsoldabove): eJUYED19
=>base50 LIGHT; jSTRC38=>base100; nZLORFIK75=>base200; JHACKEM38=>base100.
rGOLDEN56=>base150; yBUBBLY113=>base300; S MAGENTA75=>base200. A cursedbubbly
sametypey. mBAG1=>ordinarysack (notBOH/oilskin). qharp19=>wooden, sold.
Generalstore stock: bag29,24 price4; sling30,24; brilliantbluepotion31,24price67
(base50); tripe31,25; food29,26; tinwhistle30,26price13; longsword31,26.
Our soldq28,26; soldE/C/l28,25. No usefulmagicstock. Remainingfood2rations
29,25/30,25BOUGHTgone. Nodebt. Door35,23LOCKED,nymph33,25insideavoid.
Horseandcatoutsidegeneralstore closeddoor27,24. Warhorsefoughtwatchcaptain6967
thenfollowed, noheroanger. OBS4h02m34healthy. ContinuingnextMineslevelnewpick.

OLDER:
LATEST T6920: MINETOWN Dlvl7 hero40,17. HP55/60 XL6/525 AC-4 $21 bagempty.
Werewolf killed6912 after confusion potion, confusion gone, no infection.
FOURTH prayer6900 at LAWFUL staffed Tyr temple uncursed old helm; now wearing
N blessed dwarvish iron helm (likely +1), old i +0 orcish helm on altar.
Altar47,21 templefloor45..48,19..22 entrance48,18. Priest peaceful.
ALTAR STASH: cursed pickt, cursed circular amuleth, oldhelm i, gems x/D/k.
All other items retrieved: e/j/n/J unknownscrolls UNCursed, L2blank,
lCURSEDspeedpotion, r/y/Suncursedgolden/bubbly/magenta, A cursedbubbly,
Iuncursedoctagonalamulet. aExcalibur+1, cshield+3,u/v/B/O armorunchanged.
E striking EMPTY,zcreatemonster,memptybag,qharp,Kblindfold,UordinaryTINwhistle.
Food Qlembas,Tfoodration,Vfoodration,W1slimemold. Lastatecoyote6371.
Patjitan deli entrance51,18, food purchased PAID6870, no debt. Warhorse
attacked merchant and took many hits but escapedalive6880; keepaway shops!
Warhorse43,17 current, housecat behindnearwerewolfcorpse48,17. Bothalive.
Minetown UP77,17 DOWN11,13. Teleporttrap18,15. Routeup77,17->69,16->66,16
->65,15->58,14->58,16->59,17..20->door57,20->town56,20. Street26..56,17.
Other doors32,16;35,18;35,23;41,24;53,14;53,26 unexplored.
Likelyshopkeepers28,24 and40,24, mimic39,24. Watchcaptain38,14 peaceful.
Mines2 Dlvl6 UP73,25 DOWN43,16; routealongrow24westto55thenNWto43,17.
Mines1 down23,27; previoussnapshot below. OBS3h55m54 healthy. NOdeadline.

OLDER:
LATEST T6582: Mines first level Dlvl5, downstairs23,27, bothpetsadjacent,
descendingnext. HP60/60 XL6/494 AC-2 $7+120bag. Excalibur a +1 blessedrustproof.
Horse grewWARHORSE6360ish. FedlichenR T6565 successfully; Rgone. Qlembaswafer
picked6490 INPACK reserve. Herocoyotecorpseate6371, nofoodsince. Prayerlast6010.
Housecat alive fediguana6410ish. Mines entry D4down54,14 ->Mines1up39,15.
Mines1 down23,27. Fast route up39,15 ->39,19->36,19->34,18->30,15
->27,12->25,12->24,13/14->24,18->23,22->23,27. Mapmanydarkcavebends.
Spikedpit38,24 AVOID, squeakyboard47,11. Elvendagger24,14 left. Mosteast
mapexplored allway53,20/52,24; SW32,22lembasdeadend. Minedwestpassagefound
from39,19. Native '_' travel target cursor-relative keypad then '.' works!
It even found unchartedshortcut butavoidedpit; valuable forbacktracking.
OBS3h33m32 healthy. No deadline. Needcontinueplaying untiluserstop.

OLDER:
LATEST T6349: EXCALIBUR acquired sixth fountain dip D5 Oracle south40,22.
HP60/60 XL6/427 AC-2 $7+120bag. Longsword a now blessed rustproof +1Excalibur.
THIRD PRAYER T6010 relievedWeak; no prayer until cooldown safe. Ategrayoozeglob
6056 acid13HP noresgained, Pgone. Horsealive lastfed5254; kitten becameHOUSECAT
T6307. BothwithheroD5Oracle. Oracle ANGRY from gas sporeexplosion6185:
I misidentified e as floatingeye thenPK77killedspore. Oracle notattackedagain,
passiveonly sojustavoidmelee. Explicitfarlook ALLambiguousmonsters beforeattack!
Blind yellowlight6007 woreoff6110ish. Two gas spore explosions6088/6185 healed.
Wait-pets x y subcommand added bounded25search, stopsboth f/u adjacent, HPdrop,
newconditions/noTadvance. Existing blindness allowed; onlyuseverifiedsafe tile.
Plan headD4Mines forfood/altar/newpick, strongerweapon now. D6Soko/shopstillmissing.

OLDER:
LATEST T5937: D8 XL6/377 HP60/60 AC-2, $7 open +120 in bag m. Hungry.
Returning toward Oracle D5 for possible Excalibur, no dips yet. Second prayer
T5161; next Weak prayer should be safe cooldown. No food left. Horse fed5254,
kitten ate lizard5740, both alive D8. Horse following, kitten out of view.
NEW inventory: i worn orcish helm confirmed CURSED5707; N noncursed dwarvish
iron helm in pack cannot wear until i removed. O +0 dwarvish cloak worn5706.
Pick t still cursed never wielded. E striking empty. Longsword Skilled.
Prayer off altar at Luck0 fixes major troubles only: do NOT equip cursed pick
hoping hunger prayer uncurses it. Need altar/remove curse/holy water/new pick.
D7 FAST stairs route: up30,28 ->28,27->secret28,26->28,25/24/23->27,23/22
->26,22/21->25,21->25,20->down26,19. Leprechaun hall west13,21 avoid.
D8 UP45,24 floor40..47,23..26 northdoor40,22 ->40,21->41,21/20/19/18
->42,18->42,17->room36..49,13..16 DOWN36,14 (D9 unvisited).
D8 mapped six rooms no food/shop/altar. West room18..22,17..22 entry17,18,
SW4..10,21..23 entries11,21/23. NE57..65,14..15 entry56,14 exit64,16.
SE58..67,23..27 north59,22 west57,27. Spotted jelly61,21 alive bypass via
61,20->60,21->59,21 south. Boulder49,27 bypass diagonally50,27->49,26.
North highway34..51,11 ->51,13->55,14; west34,12/13 then downstairs room.
NEW compact screen lists neighbors for each @; use this for doorway coords.
OBS3h09m22 live healthy zero skipped/congestion/reconnect. No deadline.

OLDER snapshot:
LATEST T5260: D7 XL6/351 HP60/60 Pw7/7 AC-2 $82. LONGSWORD SKILLED at4668.
SECOND PRAYER T5161 relievedWeak, Tyrwellpleased. E striking wand EMPTY at5137
(zE no direction prompt so trailing4becamewalk). FoodM ration D7 picked5193,
fed STARVING HORSE onD6 T5254 successfully. Horse stillTAME confirmed5259,
now withhero D7 upstairs30,28. Kitten elsewhereD7 (followedthenwanderedoff
aroundT5244..5252, likelyheadingbeetlecorpse). Alive lastseen. FindwithPK/RK.
Horse grewfrompony4850 afterkillleprechaun; becameconfusedhunger5052, leftD6
whilefetchingration, returnfed5254 nowrescued. No food inpackagain. Pet horse
needsregularvegetarianfood, eatspeoplefoodwhenstarving. Avoidrepeatinglongsearch!
OBS2h40m51 lastchecked live healthy. Stream ongoinguntiluserstop.
D7 map: upstairs30,28 room24..32,27..28, eastdoor33,28->34..41,28,
SECRET40,28 found5075. Corridor42,27->44,26->45,25/24->59,24.
Giantbeetle58,24 killed5100, corpsePOISON leave (oldnow). Dustvortex atSE
door64,25 killed5113 ->XL6. HPmax60. Dogkilled5173 no corpse.
SEroom65..74,24..26 west64,25; north69,23 kicked open5120, north74,23
alsoopen. Northcorridor69,22/21->71,21->71..73,22 loops74,23; westbranch
69..65,22 ends BOULDER64,22 pushedwesttwice5136, blockednow, no wandcharges.
Centraljunction60,24->60..63,25->64,25; north59/60,23->59/60,22 ->59,21/20
->59,19/18/17->door58,17 room53..57,17..22 (northwall16 notshowncompact).
Box53,17 checkedonceuntrapped5198, NOTLOOTED, notcarried. Gem57,19,gold53,22
uncollected. FoodM56,18 consumedbyhorse. Westroomdoors52,18/20 UNEXPLORED.
TelepathyD7 huge LEPRECHAUNHALL3..11,18..22 (45leprechauns), avoidgoldtheft.
D6 latestsearch: startingwallsmostlycleared; SW3..11,22..25 allperimeter
searched25 exceptnorth?6,22searched25. NW secret6,15 found5040 opened5050,
deadend6,16 only1searchinterruptedhorsehunger. NW7,14=25,4,14=25;
westwallNW3,13 NOTsearched. D6 still NOshop/Sokoban. Don'tburnmorefoodsearch.
L 2unlabeledblankscrolls picked4515, KblindfoldNONCURSEDpetcarry.

OLDER T4510: D6 XL5/254 HP47/47 Pw6/6 AC-2 $20. Hero41,23, hostile paper
golem40,23 attacking. Both pets nearby. FIRST PRAYER T4324 relieved Weak,
Tyr well-pleased. No more prayers until safe cooldown (~500+ turns minimum).
K blindfold acquired NONCURSED kitten carried. PK put on, RK remove. Telepathy
revealed shopkeeper Malasgirt70,25 (peaceful), dwarf68,24, p48,27, eye55,28.
Southern level remains unexplored, no entrance found. Bluejelly killed4083,
ate4090; violetfungus4124 killed dropped blindfold. No food pack.
More search audit: 57,26=40;63,23=55;59,23=30;62,22=30;65,20=25;
68,19=25;67,20=31;69,19=25;73,18=25;41,23=25 interruptedpaper golem.
NE north59,12=25;56,12=25;53,12=35. No doors. Shop is SE, not NE.
OBS2h20m36 lastchecked healthy. Need check again soon.

OLDER T3948: D6 XL5/210 HP47/47 Pw6/6 AC-2 $20, Wi8. Both kitten and tame
pony alive. No food in pack; last ate fresh rothe T3524, ration H T3318.
Hero57,26, found secret south door57,25 from traproom57..59,20..24 at3944.
Looks like deadend; searching next. Trap57,22 spikedpit,57,20 rockfall AVOID.
E striking wand 5 charges used total (engrave +4 zaps), remaining unknown.
b dagger recovered, g4 darts, C spear, z create monster used once. I new
octagonal amulet, J HACKEM MUCHE scroll; all unknown. Still cursed pickaxe t,
never equip. No prayer used, no altar/shop/Sokoban found on D6. D5 Oracle.
OBS2h14m checked live, zero skips/congestion/reconnect, NO timed stop.
D6 seven rooms mapped: start19..24,20..22; SW4..11,22..25; NW4..10,12..14
(down10,13 toD7 unvisited); small33..39,23..25; trap57..59,20..24;
NE47..60,12..14; farEast73..75,14..18 (secret door72,17).
Exhaustive corridor searches so far no new room: 42,15=30;42,17=25;
40,18=25;37,18=29;37,20=19;34,21=25;31,21=25;28,20=25;26,18=25;
25,16=50;43,23=25;46,23=25;49,23=23;52,24=20. Deadends33,27=73,
38,27=44 (secret38,26),55,25=75. FarEastroom allwalls20..25searched.
Remaining promising: roomwalls north/south START, north/southNElarge,
west/southNW andSW, northsmall33..39,23; corridor63,23 onlysearched20;
42,14 only5search (41,13 uncovered by adjacentsearch). Need systematic
wall check, avoid repeating old endpoints. Pets often block movement!

OLDER T2826 SNAPSHOT:
LATEST T2826: D6 XL4/153 HP26/40 AC-2 $20. Hero7,13 NWdownstairsroom
4..10,12..14. Downstairs10,13. Kitten5,13 AND new TAME PONY6,13 (fed last
lichen s at2801). Gas spore8,13 killedwithsword aftermaneuveringpets3tiles
away;14blastdamagehero, NO PETdamage. Heal/searchnorthwallnow. FoodH ration
fromhillorc, G ration consumed2559. No s lichenleft. z createmonster,E striking
wand: engraving1charge +2combatshots2670ish BOTHmissedgiantant. Noescapes.
Giantant killed2666 kittenate,14damage healedbeforegas. HPmax40. Daggerbasic,
swordbasic no#enhanceavailable2596. b+0daggerinpack,g6darts,C orcishspear.
D6 startingroom19..24,20..22 upstairs22,20. SECRET westdoor18,22 found2649,
opened. Westcorridor17,22->15,22/23->14,23/24->13,24->door12,24 intoSWroom
4..11,22..25. SECRET northdoor10,21 found2795opened; corridor10,20..16->9,16
->door9,15 intoNWdownstairsroom. NoSokoban/shopfoundYET, shopkeeperheard.
D6 eastmap: startingeastdoor25,22->30,22/24->door32,24 smallroom33..39,23..25.
Southdoor33,26 deadend33,27 searched23nothing. Eastdoor40,23 longcorridor
to56,23->traproom57..59,20..24. SPIKEDPIT57,22, ROCKTRAP57,20. North57,19
**OPEN DOOR |**, notgrave! Unexplored. East60,21->62,21; southdeadend63,23
searched20nothing. North62,19..14->door61,14 NEroom47..60,12..14. Southdoor
59,15 UNEXPLORED. Westdoor46,12->45,12/14->42,14..16->41,17->37,18/21
->29,21 joinsstartingcorridor. Theseareloops. Noaltarvisited. No prayersused.
OBS1h45m05s lastchecked,0drops/congestion/reconnect. Stillliveuntiluserstop.

OLDER T2396 SNAPSHOT:
LATEST T2396: D6, XL4/98 HP40/40 Pw5/5 AC-2 $17, Co now18. Kitten moving,
withhero. Startingroom18..24,20..22; upstairs22,20. Hero24,22, eastdoor25,22
opened, exploringnext. Pickedfoodration G, have s ONElichencorpse left (ate
otherT2346), more food urgent but not starving. bdagger, g6darts, C orcishspear.
E balsa wand **STRIKING** engravetested T2363 (fightswriting), typecalledstriking,
noncursedpetcarried. z createmonster wand, remainingchargesunknown. B +0 high
boots nowworn (noncursedpetcarry), wlowbootsdroppedD5NWroom15,14. Bag m
openedEMPTY, noncursedpetcarry, sack/oilskin/holdingunknown, NOTtricks. Noitems
putinsideyet. D redgemnew. Telepathy yes; nohealing/escape/prayersused.
D5 downstairs70,25, SEroom70..74,24..28, darttrap73,27. Upstairs62,13 east
exit66,14->67,14/15->68,15..27->door69,27. NorthSEdoor71,23unexplored.
D5 NWroom8..20,13..16 onlyexit14,17 to14,18->17,20->19,20->19,21 eye room.
Eye-roomnorth21,21joins19,20loop. West17,22->16,22/23->10,23 SWroom4..9,
23..25 gemcleared, nootherexits. D5 muchcleared; noaltar/shop.
OBS1h30m55s lastcheckzeroissues; continueuntiluserstop.

OLDER T1962 SNAPSHOT:
LATEST T1962: D5 Delphi, XL4/85 HP40/40 Pw5/5 AC-1 $11. Hero19,24;
kitten21,24 frozen by floating eye since ~1885, alive. Eye killed1943,
corpse eaten1949: TELEPATHY acquired. Two manes killed, wand z engraving
identified CREATE MONSTER; spawned two gridbugs, one remains19,23 at1962.
Kill it and wait for kitten. Dagger b recovered, g6darts, z noncursed wand
(pet carried). New y/A bubbly potions different BUC, x blue gem. Same
armor/equipment/food as T1601, t CURSED pickaxe retrieved, never wield/apply.
D4 MAIN downstairs33,12 room28..35,12..16; boulder34,13. D4 other stairs
54,14 likely Mines, not visited. Main D5 upstairs62,13; westdoor59,14 leads
53,14->52,16->51,17->47,17, entrance Delphi46,18. Delphi outerroom35..45,
17..25; statues C, Oracle40,21, fountains innerroom. Westexit34,21 deadend30,21
searched35. North loop47,14/15 to36,14/15, SECRET passage35,15 discovered.
West via33,15 black naga corpse (acidic, left),32,15 south32,17->29,17->28,18
->26,18/19->24,20/22->23,22->hidden door22,22 kicked, currentroom18..21,22..25.
North exits19,21 and21,21; west17,22 unexplored. Wand/potion collected here.
No D5 downstairs found yet. Goal D6/Sokoban food. Last rationT1550,
redmoldT1729 (rotted blind, recovered), eyeT1949. Two lichen corpses backup.
Bag m unknown/uninspected; noncursed harp q; no knownhealing/escape.
No prayers used. OBS lastcheck1h19m31s, zero drops/congestion/reconnects.

OLDER T1601 SNAPSHOT:
LATEST T1601: Dlvl4 XL3/41 HP34/34 Pw4/4 AC-1 $7. Leaving Siverek armor shop.
Bought u +2 leather gloves, v +0 leather armor, w +0 low boots, ALL WORN.
Paid55 gold, NO DEBT. Sold o crested helmet for19 (on shopfloor68,15).
Shop66,15 entrance; floor67..72,14..17. Mimics71,16 and71,17 avoid. Mithril
coat72,17 costs320. Pick-axe t left65,15 outside then retrieving; **CURSED**
proven by kitten stepping reluctantly over it. DO NOT WIELD/APPLY/AUTODIG WITH IT.
D4 upstairs56,24, startingroom53..56,21..24. Westcloseddoor52,22 unvisited.
Northdoor54,20 corridor53,19..17 to53,16 door kickedopen. Tinyroom52..54,13..15
downstairs54,14. Eastdoor55,13->60,13->61,14/15->65,15->armor shop66,15.
Remainingfood: s TWO lichen corpses. Ration f eatenT1550. Last meal recent,
enough nutrition for several hundred turns. Both d/f rations now gone.
Also r goldenpotion, l orangepotion, three unknownscrolls e/j/n, h amulet,
m bag stilluninspected, q noncursedharp, k violetgem, g10darts, b+0daggerquivered.
No wands, no knownhealing/escape, no prayersused. WeakearlyHP now improved.
OBS50m39s stilllive,0drops/reconnecting. Keepgoinguntiluserstop, nodewatchdogdead.
D3 furthernotes: downstairs32,15 northroom25..33,13..15. Rocktrap30,14 (pile
rocks) andrusttrap27,15. Smallbox35,24 locked; three trapchecksfoundnone.
Magictrap23,25 inlargesouthwestroom14..24,23..26 blinded/deafened/summoned
monsters; retreated successfully, ALL status recovered, kittenalive.
Boulder9,17 bypassable diagonal; northwesttinyroom5..7,12..15 clearedgold/potion.

OLDER T1241 SNAPSHOT:
LATEST T1241: Dlvl3, XL2/35, HP19/24 Pw3/3 AC5 $11. Hero38,27, kitten39,27.
Orcish helm i now worn +0. Food ration d consumed T759, fresh newt eaten T713.
f remaining food ration. New o crested helmet UNIDENTIFIED DO NOT WEAR,
q harp (pet carried so noncursed), b dagger is now quivered, not alternate.
D3 upstairs55,18. Empty east room64..67,21..25 loops to upstairs eastdoor57,16.
North corridor58,13 west to43,13 then42,14->35,14, CLOSED DOOR34,14 unvisited.
South winding corridor35,15..19 then33,20..21,32,22..25 leads small room
34..36,24..27. LOCKED LARGE BOX35,24 checked for traps three times, none found,
not opened. Harp taken from35,25. East door37,25 corridor returns to upstairs
west exit45,16. East exit37,27 leads long dead end52,26; searched once15, no
further passage. West exit33,27 still unexplored; currently heading there.
IMPORTANT MISTAKE: treated e glyph as floating eye without far-look; actually
gas spore at43,27, threw dagger adjacent and explosion hit17 damage to7HP.
Recovered dagger b, healed to19 then lichen appeared. ALWAYS far-look ambiguous
monsters with `;` then relative keypad movements then `.`. Example `;4.` looks
one square west, identifies species without consuming time. Lichen killed.
G<direction> runs and auto-turns corridors, stops near doors/items/monsters;
much more efficient than digit batches! Safe for quiet exploration, inspect
stops. Do not append search/combat to movement unless endpoint verified.
OBS confirmed live beyond canceled30minute cutoff:33m08s,0drops/reconnects.

OLDER snapshots below, superseded by latest above:
St17 Dx15 Co17 In10 Wi7 Ch9. HP18/18 Pw1/1 AC6 Xp1/7. $11.
At turn 569 on Dlvl2; leaving NE weapons shop, returning toward downstairs.
Kitten alive nearby. No adverse conditions. Confirm current screen.

Inventory: a uncursed +1 long sword wielded; b uncursed +0 dagger alternate;
c blessed +3 small shield worn; d uncursed food ration; e unidentified scroll
JUYED AWK YACC; f food ration BUC unknown; g 10 darts BUC/enchantment unknown;
h circular amulet, identity/BUC unknown, NOT worn; i orcish helm BUC/enchantment
unknown, NOT worn. Helmet pet check inconclusive; don't treat as uncursed.
No consumables used. Goblin and jackal killed; goblin cursed orcish dagger left
behind on D1 (it welded to the goblin's hand). Kitten ate its corpse.

Update T569: HP18/18 Xp1/9. Also carrying j scroll STRC PRST SKRZ KRK,
k violet gem, l orange potion, m unknown bag (not applied), n scroll ZLORFIK.
D2 shop found northeast at x72..77,y14..19, entrance75,20. Corignac weapons
shop; no purchases or debts. The lone armor glyph at74,15 was a small mimic!
Revealed then retreated without fighting; do not approach until stronger.
D2 downstairs36,16, fountain37,16. Hidden passage34,25 connects eastern half.
Loot rooms36..39,27..28 and50..63,23..26 cleared. Empty NE room52..61,13..16
has west closed door51,16 (next to explore). East door62,14 leads twisting
corridors via63,19 /65,20 /67,21 /70,21 to SE room70..74,24..26. Other exit
72,23 leads72,21->75,21->shop75,20. A hidden passage64,19 just joins a loop.
Kitten alive. D2 unusually quiet; aim to gain XP/armor before going far deeper.

D1 explored four rooms linked by twisting corridors. Downstairs hidden behind a
locked door, kicked open. Sink in second room; no shops/altars found. Several
side exits still unexplored, especially around starting room.
D2 upstairs in tiny room on west side: hero arrived at screen x6,y19 (curses
144x36). South exit at x7,y20; boulder moved east from x8,y22 to x9,y22. Room east
door at x8,y18 remains unexplored. All these coordinates are screen positions.

Use `python3 scripts/session.py keys --compact ...` for concise screen output:
keeps numbered rows and first 82 columns (map/messages/status), drops inventory.
Use full `screen` or `i` when inventory/details matter. Compact omits purely
horizontal border lines, so inspect full map if exact walls matter.
Number-pad controls: 1/2/3/4/6/7/8/9, `n10s` repeats search and stops on threats.
Batch routine movement; inspect new prompts/combat. Curses `>>` needs Space.
Keep public notes current with `session.py note`; visible AI disclosure is fixed.
