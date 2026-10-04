#!/usr/bin/env python3
"""Render the provisional, off-app Phase 1 motion contracts and study.

This is an editable authoring tool. It neither imports nor changes app code.
All positions are a deterministic function of time. No approved production
illustration, voice or implementation is implied by these schematic outputs.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/production/picnic-v1/motion"
SIZE = (1440, 1080)
FPS = 30
DURATION = 4.8
FRAMES = int(FPS * DURATION)
BG = "#FFF9ED"
INK = "#23433D"
GREEN = "#DDEADD"
PINK = "#DD6673"
GOLD = "#DDA34A"
BLUE = "#7EACC2"
FONT = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")
FONT_FALLBACK = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SOURCE = [(210, 505), (380, 505), (550, 505), (210, 680), (380, 680)]
DEST = [(900, 505), (1070, 505), (1240, 505), (900, 680), (1070, 680), (1240, 680)]
ID_PREFIX = "CNT-01-piece-"
ACTIVE = 2  # Third source berry has an unobstructed route to basket slot-01.


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def font(size=24, bold=False):
    path = BOLD if bold else FONT
    return ImageFont.truetype(str(path if path.exists() else FONT_FALLBACK), size)


def text(d, xy, value, size=24, fill=INK, bold=False, anchor=None):
    d.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)


def wrap(d, value, width, size):
    words, lines, line = value.split(), [], ""
    for word in words:
        proposed = f"{line} {word}".strip()
        if d.textlength(proposed, font=font(size)) > width and line:
            lines.append(line)
            line = word
        else:
            line = proposed
    return lines + ([line] if line else [])


def paragraph(d, xy, value, width, size=24, fill=INK):
    x, y = xy
    for line in wrap(d, value, width, size):
        text(d, (x, y), line, size, fill)
        y += size * 1.35
    return y


def berry(d, center, radius=39, scale=1.0, highlight=False, muted=False):
    x, y = center
    r = radius * scale
    if highlight:
        d.ellipse((x-r-12, y-r-12, x+r+12, y+r+12), outline=GOLD, width=5)
    col = "#E39BA1" if muted else PINK
    d.ellipse((x-r, y-r*.93, x+r, y+r), fill=col)
    d.ellipse((x-r*.62, y-r*.68, x-r*.18, y-r*.24), fill="#F4A7AE")
    d.polygon([(x-r*.2, y-r*.85), (x-r*.65, y-r*1.13), (x-r*.03, y-r*1.03)], fill="#50795A")
    d.polygon([(x-r*.07, y-r*.9), (x+r*.18, y-r*1.26), (x+r*.47, y-r*.99)], fill="#50795A")
    for dx, dy in [(-.37,.13), (.2,.0), (.41,.4), (-.15,.55)]:
        d.ellipse((x+r*dx-2.5, y+r*dy-3.2, x+r*dx+2.5, y+r*dy+3.2), fill="#A54157")


def pip(d, x, y, pleased=False, greeting=False):
    """Direction-neutral proxy; not a selected Pip illustration or rig."""
    d.ellipse((x-75,y-165,x-22,y-42), fill="#DCD3BD", outline=INK, width=3)
    d.ellipse((x+2,y-171,x+55,y-49), fill="#DCD3BD", outline=INK, width=3)
    d.ellipse((x-87,y-77,x+82,y+98), fill="#E7DFCB", outline=INK, width=3)
    d.ellipse((x-42,y-1,x-32,y+9), fill=INK)
    d.ellipse((x+26,y-1,x+36,y+9), fill=INK)
    d.ellipse((x-8,y+27,x+6,y+36), fill=PINK)
    d.arc((x-20,y+26,x+20,y+63), 20, 160, fill=INK, width=3)
    if pleased:
        d.arc((x-46,y-4,x-24,y+15), 185, 350, fill=INK, width=3)
        d.arc((x+22,y-4,x+44,y+15), 185, 350, fill=INK, width=3)
    d.rounded_rectangle((x-66,y+84,x+60,y+139), 26, fill="#7F9E88", outline=INK, width=3)
    if greeting:
        d.ellipse((x+61,y+32,x+100,y+77), fill="#E7DFCB", outline=INK, width=3)


def base(title, subtitle):
    im = Image.new("RGB", SIZE, BG)
    d = ImageDraw.Draw(im)
    text(d, (58, 40), title, 38, bold=True)
    text(d, (58, 91), subtitle, 22, fill="#64796F")
    d.rounded_rectangle((48,145,1392,936), 38, fill="#F0F5E8", outline="#CAD9C4", width=3)
    text(d, (60,974), "PHASE 1 • PENDING HUMAN REVIEW • OFF-APP SCHEMATIC", 22, bold=True)
    text(d, (60,1010), "No selected illustration pack. No native animation implementation. Silent study.", 21, fill="#64796F")
    return im, d


def target(d, n=3, label="Given quantity • not movable"):
    d.rounded_rectangle((505,180,935,320), 30, fill="#FFF0C9", outline=GOLD, width=4)
    for i in range(n):
        berry(d, (620+i*100,251), 25)
    text(d, (720,291), label, 16, anchor="mm")
    d.line((720,325,720,365), fill=GOLD, width=7)
    d.polygon([(706,354),(734,354),(720,373)], fill=GOLD)


def tray(d, label="Available pieces", bounds=(135,400,650,792)):
    d.rounded_rectangle(bounds, 45, fill="#E6D8BB", outline="#BEA980", width=5)
    x0,y0,x1,y1=bounds
    text(d, ((x0+x1)/2,y0+38), label, 24, anchor="mm", bold=True)


def basket(d, label="Basket"):
    # Back, interior and front are separate named layers in the contract.
    # The basket front starts below the lowest full fruit silhouette.
    d.arc((795,340,1325,873), 183, 357, fill="#A98652", width=18)
    d.rounded_rectangle((790,400,1330,805), 48, fill="#FAE8BF", outline="#B7935C", width=5)
    text(d, (1060,439), label, 24, anchor="mm", bold=True)
    d.rounded_rectangle((786,770,1334,805), 16, fill="#CCA76B", outline="#A98652", width=4)
    for x in range(815,1320,34):
        d.line((x,779,x+17,799), fill="#A98652", width=2)


def ease(p):
    p=max(0.0,min(1.0,p))
    return p*p*(3-2*p)


def path_point(p, start, end):
    q=ease(p)
    x=start[0]+(end[0]-start[0])*q
    y=start[1]+(end[1]-start[1])*q-120*math.sin(math.pi*q)
    return (x,y)


def state_at(t, reduced=False):
    # Semantic ownership changes at accepted input; visual interpolation is
    # presentation only. The sample intentionally does not complete target 3.
    move, move_end, settled, ret, ret_end, ret_settled=.72,1.08,1.22,2.88,3.24,3.38
    if t < move:
        xy,scale,phase,region=SOURCE[ACTIVE],1.0,"Ready: five pieces; basket empty","tray"
    elif t < move_end:
        xy=DEST[0] if reduced else path_point((t-move)/(move_end-move), SOURCE[ACTIVE], DEST[0])
        scale=1.0 if reduced else 1.0+.06*math.sin(math.pi*(t-move)/(move_end-move))
        phase,region="Pickup: one stable occurrence moves","basket"
    elif t < settled:
        xy=DEST[0]
        scale=1.0 if reduced else 1.0+.035*math.sin(math.pi*(t-move_end)/(settled-move_end))
        phase,region="Settle: position held; no new math event","basket"
    elif t < ret:
        xy,scale,phase,region=DEST[0],1.0,"Placed: all five working pieces remain visible","basket"
    elif t < ret_end:
        xy=SOURCE[ACTIVE] if reduced else path_point((t-ret)/(ret_end-ret), DEST[0], SOURCE[ACTIVE])
        scale=1.0 if reduced else 1.0+.06*math.sin(math.pi*(t-ret)/(ret_end-ret))
        phase,region="Return: same occurrence; original source anchor","tray"
    elif t < ret_settled:
        xy=SOURCE[ACTIVE]
        scale=1.0 if reduced else 1.0+.035*math.sin(math.pi*(t-ret_end)/(ret_settled-ret_end))
        phase,region="Return settle: stable anchor restored","tray"
    else:
        xy,scale,phase,region=SOURCE[ACTIVE],1.0,"Returned: target unchanged; basket empty","tray"
    pieces=[{"id":ID_PREFIX+f"{i+1:02d}","region":"tray","slot":f"slot-{i+1:02d}","center_px":list(pos),"scale":1.0} for i,pos in enumerate(SOURCE)]
    pieces[ACTIVE].update(region=region,slot="slot-01" if region=="basket" else "slot-03",center_px=[round(xy[0],3),round(xy[1],3)],scale=round(scale,5))
    return {"time_seconds":round(t,5),"phase":phase,"pieces":pieces,"target_reference_count":3,"working_count":5,"basket_count":int(region=="basket")}


def render_m01(t, reduced=False):
    s=state_at(t,reduced)
    im,d=base("M01  Pickup / return / settle", "Reduced Motion • instant positions, no scale or travel" if reduced else "Short deterministic study • 360 ms travel + 140 ms settle")
    target(d)
    tray(d)
    basket(d)
    for i,p in enumerate(s["pieces"]):
        if i!=ACTIVE:
            berry(d,p["center_px"],39)
    # The travel layer is above containers. Never occlude a fruit under a rim.
    p=s["pieces"][ACTIVE]
    outlined=(.72<=t<.84 or 2.88<=t<3.0) if reduced else (.72<=t<1.22 or 2.88<=t<3.38)
    berry(d,p["center_px"],39,p["scale"],highlight=outlined)
    text(d,(720,864),s["phase"],24,anchor="mm",bold=True)
    text(d,(720,902),"Review annotation: IDs 01–05 persist; the three small target berries are a reference.",19,anchor="mm",fill="#64796F")
    return im


def render_join(beat):
    im,d=base("M02  Join / separate", "Two original regions • one shared region • no automatic total before response")
    positions=[(280,505),(280,665),(1120,580)]
    d.rounded_rectangle((150,380,445,755),36,fill="#E6D8BB",outline="#BEA980",width=4)
    d.rounded_rectangle((980,380,1280,755),36,fill="#D8E5ED",outline=BLUE,width=4)
    d.rounded_rectangle((500,380,900,755),36,fill="#E1EDD2",outline="#8AA973",width=4)
    text(d,(300,423),"Source",24,anchor="mm",bold=True)
    text(d,(1130,423),"Incoming",24,anchor="mm",bold=True)
    text(d,(700,423),"Shared mat",24,anchor="mm",bold=True)
    dest=[(595,525),(800,525),(700,650)]
    for i in range(3):
        xy=positions[i] if beat==0 or beat==2 else dest[i]
        berry(d,xy,39)
    text(d,(720,850),["Before: every piece has an original anchor","After join: request a response; no total label","After three returns/Undos: exact identities restored"][beat],23,anchor="mm",bold=True)
    return im


def render_share(beat):
    im,d=base("M03  Share / remainder", "Five pieces • transfer two • withhold the assessed source remainder")
    target(d,2,"Given transfer • not the remainder")
    tray(d,"Source mat")
    d.ellipse((795,420,1325,805),fill="#DCEAF1",outline=BLUE,width=6)
    text(d,(1060,450),"Friend's plate",24,anchor="mm",bold=True)
    for i,pos in enumerate(SOURCE):
        if beat==1 and i<2:
            berry(d,DEST[i],39)
        else:
            berry(d,pos,39)
    text(d,(720,855),["Before: transfer model is given","After transfer: source remainder stays unlabelled","After two Undos: original source slots restored"][beat],23,anchor="mm",bold=True)
    return im


def render_help(beat):
    im,d=base("M04  Help / demonstration", "Requested cue/model only • the demonstration never silently moves a piece")
    target(d)
    tray(d)
    basket(d)
    for i in range(5):
        pos=DEST[i] if i<2 else SOURCE[i]
        berry(d,pos,39,highlight=beat==1 and i==0)
    if beat==0:
        d.rounded_rectangle((495,170,945,330),35,outline=GOLD,width=6)
    elif beat==1:
        d.line((900,575,900,610),fill=GOLD,width=6)
        d.polygon([(884,603),(916,603),(900,622)],fill=GOLD)
    text(d,(720,855),["Cue: focus reference; no move","Model: highlight a stable destination occurrence","Cancel: remove cue; semantic arrangement unchanged"][beat],23,anchor="mm",bold=True)
    return im


def render_completion(beat):
    im,d=base("M05  Completion", "A valid explicit response precedes presentation • celebrate once per checkpoint")
    target(d)
    tray(d)
    basket(d)
    for i in range(5):
        berry(d, DEST[i] if i<3 else SOURCE[i],39)
    d.rounded_rectangle((590,830,850,905),25,fill="#588766" if beat else "#7B9988")
    text(d,(720,866),"Done" if beat==0 else "Continue",26,fill="white",bold=True,anchor="mm")
    if beat:
        for x,y in [(695,350),(747,365),(1250,343)]:
            d.line((x-10,y,x+10,y),fill=GOLD,width=4)
            d.line((x,y-10,x,y+10),fill=GOLD,width=4)
    text(d,(720,358),["Ready: exact set; no automatic success","Response accepted: glow only; controls remain live","Settled: completed state already persisted"][beat],20,anchor="mm",bold=True)
    return im


def pinwheel(d,x,y,angle=0):
    d.rounded_rectangle((x-8,y,x+8,y+235),8,fill="#AE8F5D")
    d.ellipse((x-58,y+220,x+58,y+245),fill="#98B884")
    for i,col in enumerate(["#EAB76B","#E5838C","#80B9B6","#A4B27A"]):
        theta=angle+i*math.pi/2
        pts=[]
        for xx,yy in [(0,0),(0,-110),(95,-58)]:
            pts.append((x+xx*math.cos(theta)-yy*math.sin(theta),y+xx*math.sin(theta)+yy*math.cos(theta)))
        d.polygon(pts,fill=col)
    d.ellipse((x-15,y-15,x+15,y+15),fill=INK)


def render_garden(beat):
    im,d=base("M06  Garden / spin / bloom", "Stable toy instances • rotor-only pivot • flower has aligned bud/open states")
    d.rounded_rectangle((90,650,1350,900),36,fill="#C5D9AC")
    x=[350,565,565][beat]
    pinwheel(d,x,470,[0,math.pi*.7,math.pi*2][beat])
    d.line((1010,590,1010,825),fill="#5F8B63",width=13)
    if beat==0:
        d.ellipse((977,535,1043,615),fill=PINK)
    else:
        for a in range(6):
            theta=a*math.pi/3
            cx,cy=1010+56*math.cos(theta),573+56*math.sin(theta)
            d.ellipse((cx-31,cy-31,cx+31,cy+31),fill=PINK)
        d.ellipse((985,548,1035,598),fill="#EFBE69")
    text(d,(720,240),"Toy identity and earned ownership never change on an animation callback.",24,anchor="mm",bold=True)
    text(d,(720,855),["Before: free flower bud; earned pinwheel placed","Interaction: one bounded rotor turn / flower opens","End: toy placements persist; no infinite spinning"][beat],22,anchor="mm",bold=True)
    return im


def render_greeting(beat):
    im,d=base("M07  Greeting / farewell", "Aligned still-pose proxy • no articulated rig or approval of Pip's identity")
    d.ellipse((565,758,875,803),fill="#D2DFC5")
    pip(d,720,575,pleased=beat==1,greeting=beat==1)
    text(d,(720,267),["Ready pose","Single friendly pose transition","Return to calm / exit remains immediate"][beat],29,anchor="mm",bold=True)
    text(d,(720,847),"1536 × 1536 aligned pose masters planned; foot anchor and gaze must be reviewed.",22,anchor="mm")
    return im


LAYER_SHARED = [
    {"id":"environment-distant","z":0,"pivot":"canvas origin","contract":"Decorative only; no labels or countable fruit."},
    {"id":"environment-ground","z":10,"pivot":"canvas origin","contract":"Aligned with distant and foreground; semantic safe regions remain clear."},
    {"id":"environment-edge-foreground","z":60,"pivot":"canvas origin","contract":"Never crosses the working-region or target safe masks."},
    {"id":"controls-and-reference","z":100,"pivot":"native bounds center","contract":"Given count/transfer only. Native UI outside background art; persistent input stays live."},
]


def layer(i,z,pivot,contract):
    return {"id":i,"z":z,"pivot":pivot,"contract":contract}


COMMON = {
    "schema_version":"phase1-motion-brief-v1",
    "version":1,
    "status":"provisional-pending-human-review",
    "selected_take":None,
    "working_concept":"Pip's Picnic; comparison concept, not approved final identity",
    "implementation":"Authoring specification and off-app schematic only. Future behavior is native SwiftUI; no native implementation is present here.",
    "coordinate_system":{"production_proposal":"Normalized layer coordinates, origin top-left, x/y in [0,1]. Local pivot maps named per layer.","study_canvas_px":[1440,1080]},
    "semantic_state_ownership":{
        "owner":"Future native activity/reward model, never the animation renderer.",
        "commit_rule":"An accepted tap/drag/Undo changes persistent region/slot/history or reward ownership exactly once before presentation. Invalid/cancelled input commits nothing.",
        "excluded_from_animation_completion":["quantity mutation","new occurrence creation","response correctness","missCount","help attribution","checkpoint completion","reward grant","session completion","history writes"],
        "completion_callbacks":"May clear ephemeral visual transforms only. Must not create mathematical evidence or grant a reward.",
        "identity":"Namespace authored occurrence templates by round ID. Same occurrence ID, object family and origin anchor survive move, return, Undo, pause, rotation and resume.",
        "audio_invalidation":"Accepted object movement cancels stale prompt/help/count speech. When enabled, latest basket or friend's-plate count replaces earlier counts. Never speak an assessed joining total or source remainder automatically.",
        "rendering":"A moving occurrence is rendered once on the travel layer, never duplicated at source and destination. Target-reference copies are explicitly noninteractive and excluded from the working set."
    },
    "global_interrupts":{"navigation_background_system_interruption":"Stop narration/effects and presentation. Persist committed semantic state. Resume silently at exact current anchors; no replay or delayed completion event.","rapid_input":"Input never waits for travel/celebration. Replace the affected occurrence's visual trajectory from its sampled visible position toward the latest committed anchor; do not run a FIFO animation or speech backlog.","gesture_cancellation":"Cancel transient drag without a semantic move; return to the committed anchor. Do not record a mathematical miss.","reduced_motion_toggle":"Cancel travel/scale/rotation and snap to the latest committed semantic state. Preserve goal, object visibility and live controls."},
    "sound_contract":{"required_for_meaning":False,"music":"excluded","settings":"Narration, spoken-count and effects controls are separate.","cues":"Optional effects only on accepted actions; no source SFX generated for this Phase 1 study. System/accessibility announcements must not overlap the prerecorded lane."},
    "human_review":{"art":"pending","content":"pending","motion_comfort":"pending","child_usability":"pending","native_layer_pack":"not-produced"},
    "provenance":{"method":"Original direction-neutral Pillow vector schematic, deterministic timeline; no generative provider or experiment assets imported.","source_script":"scripts/phase1-motion-study.py","rights":"Original schematic recipe. Arial is used from the local OS only for adult review rasterization, not redistributed or selected as app typography.","source_references":["docs/planning/asset-register.csv","docs/planning/content-catalog.json","docs/planning/asset-production-plan.md"],"human_approval":False},
}


SPECS = {
 "M01":{
  "name":"pickup-and-return","dependencies":["OBJ-BERRY","OBJ-APPLE","PROP-BASKET","LAYOUT-COUNT","REF-00","REF-01","REF-02","REF-03","REF-04","REF-05"],
  "triggers":["Accepted tap-to-move into basket","Accepted return tap or Undo","Accepted drop if optional drag is later approved"],
  "layers":LAYER_SHARED+[layer("basket-back",20,"normalized (0.5,1.0)","Aligned with front; the interior slot mask stays visible."),layer("stationary-occurrences",30,"each fruit center (0.5,0.5)","Up to six distinct stable occurrences; no silhouette overlap."),layer("basket-front",40,"normalized (0.5,1.0)","Rim is below every fruit's full silhouette; cannot conceal stems/seeds or working count."),layer("moving-occurrence",50,"same fruit center","Exactly one instance; above prop edges and below UI. No trails, clone or squash that reads as another piece.")],
  "start_state":"CNT-01: target model 3; five unique berries in original tray slots; basket empty.",
  "middle_state":"One accepted move commits piece-03 to basket slot-01; presentation travels and settles. Four other identities stay fixed.",
  "end_state":"Return/Undo restores the same piece-03 to original tray slot-03. Target stays 3; basket empty; all five pieces visible. This sample does not submit or complete the activity.",
  "duration_ms":{"travel":360,"settle":140,"per_move_total":500,"sample_total":4800},
  "repeat_policy":"Once per accepted semantic move/return; no idle repeat. A reverse input retargets immediately.",
  "motion_recipe":"Smooth cubic travel with shallow upward arc; maximum scale 1.06; settle 1.035 to 1.0. No bounce off boundaries or occlusion under the basket rim.",
  "reduced_motion":"Immediate single-instance reposition at accepted input; fixed scale 1.0. Optional static selected outline for at most 120 ms, no travel/bounce.",
  "occlusion_contract":"Study front rim top y=770; maximum settled fruit bottom <724. Motion path remains above rim. Future layer pack must confirm this at all six slots in both orientations.",
  "sound_cues":["SFX-PICKUP optionally at accepted move","SFX-PLACE optionally at anchor arrival, cancel if retargeted; no model mutation on cue","Configured current basket count is latest-only and optional"],
  "storyboard_beats":["Before pickup","Moved and settled","Returned and settled"],
 },
 "M02":{
  "name":"join-and-separate","dependencies":["OBJ-BERRY","OBJ-APPLE","PROP-MAT-A","PROP-MAT-B","LAYOUT-JOIN"],
  "triggers":["Accepted move from source/incoming to shared mat","Accepted return or Undo"],
  "layers":LAYER_SHARED+[layer("source-mat",20,"bounds center","Distinct original region/anchor; non-color location cue."),layer("incoming-mat",20,"bounds center","Separate from source/shared; preserves original region."),layer("shared-mat",20,"bounds center","Not an automatic answer label."),layer("stationary-occurrences",30,"fruit center","All pieces countable and separate; no merge/morph."),layer("moving-occurrence",50,"fruit center","One persistent instance crosses regions; no numeric total attached.")],
  "start_state":"Example JOIN-01: two source occurrences and one incoming occurrence, each with its original region/slot.",
  "middle_state":"All three occurrences share distinct shared-mat slots. In a numeral-total variant ask for a response; do not automatically expose/speak the assessed total.",
  "end_state":"Undo restores the exact prior occurrence region/slot; separation never creates replacement pieces.",
  "duration_ms":{"travel":360,"settle":100,"per_move_total":460},
  "repeat_policy":"One travel per accepted move; simultaneous accepted actions may have independent paths without blocking input.",
  "motion_recipe":"Same restraint as M01; source/incoming remain visible. Route moving silhouettes away from occupied slots; no collective merging.",
  "reduced_motion":"Immediate reprojected positions and static region focus. No arc, scaling or sequential count reveal.",
  "occlusion_contract":"No piece behind a mat, another fruit, Pip, edge scenery or UI. Shared total is visually countable but not supplied as a numeral/automatic speech answer.",
  "sound_cues":["Optional pickup/place effects only","No automatic shared-total narration; requested model has support metadata"],
  "storyboard_beats":["Original regions","Joined; answer withheld","Undo to original regions"],
 },
 "M03":{
  "name":"share-and-remainder","dependencies":["OBJ-BERRY","OBJ-APPLE","PROP-MAT-A","PROP-PLATE","LAYOUT-TAKE","REF-00","REF-01","REF-02","REF-03","REF-04","REF-05"],
  "triggers":["Accepted transfer to friend's plate","Accepted return/Undo","Explicit checkpoint transition to remainder question"],
  "layers":LAYER_SHARED+[layer("source-mat",20,"bounds center","Remainder pieces remain fixed and visible; no total label before assessment."),layer("friend-plate",20,"bounds center","Distinct target destination; no rim covers fruit."),layer("stationary-occurrences",30,"fruit center","Identity and source return anchors persisted."),layer("moving-occurrence",50,"fruit center","One instance; no clone/fading countable residue."),layer("checkpoint-focus",80,"region bounds","Transfer target is given; remainder focus contains no answer numeral/equation.")],
  "start_state":"Example TAKE-01: five source berries; separate given reference requests two transfers.",
  "middle_state":"Two stable identities are on the friend's plate. Three source identities remain visible; the assessed remainder is unlabelled and unspoken.",
  "end_state":"Undo restores exact original source slots. A remainder response is separate from transfer completion/help; no motion callback records either response.",
  "duration_ms":{"travel":360,"settle":100,"checkpoint_focus":180,"per_move_total":460},
  "repeat_policy":"Once per accepted transfer; focus once on explicit checkpoint entry. Zero transfer makes no fake motion or synthetic response.",
  "motion_recipe":"Shallow single-piece route to a visible plate slot. Subtle static focus border at remainder checkpoint; never march/count the source unrequested.",
  "reduced_motion":"Immediate positions; static source focus border on remainder question. Zero stays intentionally empty, without a flourish implying a piece.",
  "occlusion_contract":"Destination plate edge stays below fruit silhouettes. Source and destination do not overlap; given reference stays outside both.",
  "sound_cues":["Optional effects on accepted move","Latest plate count only when configured","No automatic source-remainder count; requested source model is recorded as help"],
  "storyboard_beats":["Given transfer model","Transfer; remainder withheld","Undo preserves all identities"],
 },
 "M04":{
  "name":"help-and-demonstration","dependencies":["PIP-02","PIP-03","CUE-DEMO","REF-00","REF-01","REF-02","REF-03","REF-04","REF-05","LAYOUT-COUNT","LAYOUT-JOIN","LAYOUT-TAKE"],
  "triggers":["Explicitly selected current-checkpoint focus cue","Explicitly requested modeled counting","Explicit help replay"],
  "layers":LAYER_SHARED+[layer("pip-aligned-pose",25,"1536 canvas foot anchor (0.5,0.90)","Aligned still pose crossfade only; warm attentive expression, never disappointed."),layer("occurrences",30,"fruit center","Do not auto-place, duplicate, hide or renumber an occurrence."),layer("focus-border",70,"reference/region bounds","Non-color cue around given reference then destination; no answer leak."),layer("cue-demo",80,"normalized tip (0.5,0.92)","Separate cursor/outline—not another fruit; at most one highlighted occurrence per modeled count.")],
  "start_state":"Committed arrangement and checkpoint evidence unchanged. User requests current-checkpoint cue/model.",
  "middle_state":"Cue focuses the given reference/destination without moving fruit. Requested model highlights actual stable occurrences in order; zero uses an empty-region focus.",
  "end_state":"Remove transient cue on finish/cancel. Arrangement unchanged; record delivered cue/model support at the relevant checkpoint when shown, not as a late callback.",
  "duration_ms":{"focus_border":180,"model_highlight_per_occurrence":550,"max_six_piece_model":3300,"pose_crossfade":160},
  "repeat_policy":"One pass per explicit request; no automatic looping or escalation. Explicit replay replaces prior help; it does not queue.",
  "motion_recipe":"Static outline then one gentle highlight per stable occurrence. No cursor teleport count ambiguity; deliberate model only may use exact number clips.",
  "reduced_motion":"Static focus border and immediate highlight steps at the same support timing. Aligned pose switch without travel, pulse or scaling.",
  "occlusion_contract":"Cue ring stays outside silhouette; finger proxy never covers the full fruit. Given reference and response choices remain discoverable.",
  "sound_cues":["Exact current-checkpoint help line optionally","Number clips in requested model carry model support; ordinary replay/Undo/current count do not automatically mean extra help"],
  "storyboard_beats":["Requested cue","Requested model highlight","Cancelled; arrangement preserved"],
 },
 "M05":{
  "name":"completion","dependencies":["PIP-04","UI-CONTINUE","REWARD-PINWHEEL"],
  "triggers":["Explicit valid response accepted and persisted by native model","Explicit Continue transitions onward"],
  "layers":LAYER_SHARED+[layer("completed-occurrences",30,"fruit center","Exact set stays still and countable during celebration."),layer("pip-aligned-pleased-pose",25,"1536 canvas foot anchor (0.5,0.90)","Same identity/scale/baseline as ready pose; no triumphant jump."),layer("completion-mark",75,"native component center","Subtle glow/check, no occlusion of quantity."),layer("celebration-specks",70,"scene safe area","Few non-countable marks outside working regions; no fruit-shaped confetti."),layer("continue-control",100,"native control bounds","Live immediately; no mandatory celebration delay.")],
  "start_state":"No automatic success on initial render, including target zero. A valid explicit Done/number response is required.",
  "middle_state":"Correctness/checkpoint completion already persisted once; show restrained pleased pose and mark. Mathematical evidence remains unchanged by celebration.",
  "end_state":"Completed arrangement remains stable. Continue is immediate. One session reward grant is owned/idempotently committed by the session model, never by animation end.",
  "duration_ms":{"pose_crossfade":160,"glow":600,"max_total":760},
  "repeat_policy":"At most once per newly completed checkpoint; repeat Done/Continue cannot replay grant/record. No idle loop.",
  "motion_recipe":"Small static mark with brief opacity/glow; no camera zoom, countable confetti or compulsory pause.",
  "reduced_motion":"Immediate pleased pose/check and live Continue. No spark travel or glow pulse; completion visible without effects/speech.",
  "occlusion_contract":"Never cover correct pieces, target, answer choices or Continue with Pip, marks or specks.",
  "sound_cues":["Optional SFX-SUCCESS once per new completion","Post-success exact explanation is presentation only; cannot rewrite earlier assistance evidence"],
  "storyboard_beats":["Explicit response ready","Persisted success presentation","Settled; Continue live"],
 },
 "M06":{
  "name":"garden-placement-spin-bloom","dependencies":["ENV-02","REWARD-PINWHEEL","REWARD-FLOWER","DECOR-01","DECOR-02","DECOR-03","DECOR-04","DECOR-05","UI-FINISH"],
  "triggers":["Accepted toy placement","Tap placed pinwheel","Tap free flower","Explicit Finish"],
  "layers":LAYER_SHARED+[layer("toy-placement-shadow",20,"toy base anchor","Decorative only; does not create a second toy."),layer("pinwheel-base",30,"normalized ground (0.5,0.98)","Stable placement bounds shared with stem."),layer("pinwheel-stem",31,"normalized base (0.5,1.0)","Stationary while rotor turns; do not spin the full toy."),layer("pinwheel-rotor",32,"normalized hub (0.5,0.5)","Exact co-registered hub pivot; rotor clear of controls/other toys."),layer("flower-bud",30,"normalized base (0.5,0.98)","Same canvas/anchor as open state; single flower instance."),layer("flower-open",30,"same base (0.5,0.98)","Crossfade alternative state; semantic toy count stays one."),layer("decorations-01…05",30,"named ground base per item","Persist placement bounds/instance IDs; stable anchor and non-overlap safe masks.")],
  "start_state":"Free flower available immediately; earned toys/placements come from persisted finite reward ownership. No fabricated seventh reward.",
  "middle_state":"One accepted placement commits anchor before 220 ms settle. Pinwheel rotor turns once around its hub; flower bud changes to open without a second instance.",
  "end_state":"Stable persistent placements; rotor angle resets modulo one turn. Flower may return to bud on an explicit next tap; Finish remains immediate.",
  "duration_ms":{"placement_settle":220,"rotor_turn":900,"flower_crossfade":280,"max_rotation_degrees":360},
  "repeat_policy":"One bounded turn per tap. A tap during spin retargets one turn from current visible angle; no FIFO queue or infinite rotor. Flower tap selects latest bud/open state.",
  "motion_recipe":"Rotor-only ease-out; at most one turn. Placement small settle, no toy drop from sky. Flower aligned state crossfade, not growth that changes bounds.",
  "reduced_motion":"Immediate placement; static hub highlight instead of spin; immediate bud/open switch. No rotational, scaling or falling movement.",
  "occlusion_contract":"Garden toy bounds and hub clearance cannot cover Finish or each other. Front scenery mask excludes placement regions. Layer sources/pivot are still provisional and unproduced.",
  "sound_cues":["Optional SFX-PINWHEEL/SFX-FLOWER on accepted toy interaction","Named earned-item line only after model owns the reward; no effect is required to identify it"],
  "storyboard_beats":["Stable toy placement / bud","Bounded rotor / open flower","Settled placements; no loop"],
 },
 "M07":{
  "name":"greeting-and-farewell","dependencies":["PIP-01","PIP-05","ENV-01","ENV-02","UI-HOME","UI-FINISH"],
  "triggers":["Fresh home entry","Explicit Finish/farewell","Resume shows calm pose silently"],
  "layers":LAYER_SHARED+[layer("pip-ready-pose",25,"1536 canvas foot anchor (0.5,0.90)","Transparent aligned still master; stable scale/gaze/feet."),layer("pip-greeting-pose",25,"same foot anchor (0.5,0.90)","Whole-pose crossfade, not an unplanned articulated arm rig."),layer("pip-farewell-pose",25,"same foot anchor (0.5,0.90)","Warm calm farewell; never implies data lost."),layer("character-shadow",20,"ground anchor","Small fixed shadow shared across poses; no jumping scale illusion.")],
  "start_state":"Stable aligned ready pose, current scene/navigation state already established.",
  "middle_state":"One friendly pose transition; greeting/farewell language optional. Controls can navigate immediately.",
  "end_state":"Return to ready or immediate requested exit. Resume is silent. Farewell neither writes progress nor deletes state; persistence belongs to native model.",
  "duration_ms":{"pose_crossfade":180,"hold":450,"return_crossfade":180,"max_total":810},
  "repeat_policy":"One greeting per fresh home entry, one farewell per explicit Finish. No idle wave loop; no replay on background resume.",
  "motion_recipe":"Aligned still-pose crossfade with fixed foot baseline. No body bob, scene travel, lip-sync rig or arbitrary pose warping.",
  "reduced_motion":"Immediate calm greeting/farewell pose; fixed anchor and no crossfade needed. Navigation never waits.",
  "occlusion_contract":"Pip's reserved region never overlaps target, fruit, choices or persistent controls in either orientation.",
  "sound_cues":["VO-WELCOME optionally on fresh entry","VO-BYE optionally on explicit Finish","No narration on resume; navigation cancels current speech"],
  "storyboard_beats":["Aligned ready","Single friendly pose","Calm return / immediate exit"],
 },
}


ORIENTATION_POLICIES = {
    "M01": "Use LAYOUT-COUNT. Landscape: tray left of basket. Portrait: tray above basket.",
    "M02": "Use LAYOUT-JOIN. Landscape: left and right source groups above a separate shared mat. Portrait: left and right source groups in the upper row, shared mat below. Do not substitute counting tray/basket regions.",
    "M03": "Use LAYOUT-TAKE. Landscape: source mat left of friend's plate. Portrait: source mat above friend's plate. The given transfer reference remains separate from both working regions.",
    "M04": "Inherit the active LAYOUT-COUNT, LAYOUT-JOIN or LAYOUT-TAKE. Reproject requested cue/model focus to that layout's reference, working region or stable occurrence. Do not rearrange semantic pieces for help.",
    "M05": "Inherit the active activity layout (LAYOUT-COUNT, LAYOUT-JOIN or LAYOUT-TAKE). Keep the completed set/response stable and the Continue control inside the current orientation's persistent control safe region.",
    "M06": "Use orientation-specific garden placement and reserved Finish bounds, not an activity layout. Reproject each persisted toy's normalized placement anchor within its safe garden region; retain its instance ID, owned state and allowed bounds. Keep rotor clearance and decoration bounds away from Finish and other toys.",
    "M07": "Use the orientation-specific reserved guide-character region and persistent control safe regions on home/garden/farewell. Reproject the aligned Pip canvas/foot anchor within its reserved region; keep the same guide identity, pose, scale relationship and gaze, clear of quantities and controls.",
}
ROTATION_POLICY = " Preserve all applicable occurrence/toy/guide identities and committed region/slot/anchor state; reproject anchors rather than repopulate. Cancel ephemeral visual interpolation on rotation and render the latest committed semantic state. Rotation never records a move, response, support event, completion or reward."


def coordinate_contract(asset_id):
    return {**COMMON["coordinate_system"],"orientation_policy":ORIENTATION_POLICIES[asset_id]+ROTATION_POLICY}


def storyboard(asset_id, frames, brief):
    folder=OUT/asset_id
    sheet=Image.new("RGB",(2400,1800),BG)
    d=ImageDraw.Draw(sheet)
    text(d,(80,58),f"{asset_id}  {brief['name']}",56,bold=True)
    text(d,(80,130),"PROVISIONAL MOTION / LAYER CONTRACT • PENDING HUMAN REVIEW",28,fill="#64796F",bold=True)
    for i,frame in enumerate(frames):
        frame.save(folder/f"storyboard-{i+1:02d}.png")
        sheet.paste(frame.resize((720,540),Image.Resampling.LANCZOS),(80+i*760,215))
        text(d,(80+i*760,782),f"{i+1}. {brief['storyboard_beats'][i]}",28,bold=True)
    y=866
    for label,key in [("Start","start_state"),("Middle","middle_state"),("End","end_state"),("Reduced Motion","reduced_motion"),("Ownership","semantic_state_ownership"),("Pending","human_review")]:
        value=brief[key]
        if key=="semantic_state_ownership": value=value["commit_rule"]+" Animation completion only clears ephemeral transforms."
        if key=="human_review": value="Human art/content/comfort/child-use decisions remain pending. Final layers/pivots and native behavior are unproduced."
        text(d,(80,y),label,28,bold=True)
        y=paragraph(d,(365,y),value,1930,28)+26
    sheet.save(folder/"storyboard-contact-sheet.png")
    sheet.save(folder/"storyboard.pdf","PDF",resolution=160.0,title=f"{asset_id} provisional Phase 1 storyboard",author="",subject="Pending human review; off-app schematic")
    dump(folder/"storyboard-source.json",{"canvas_px":[2400,1800],"render_script":"scripts/phase1-motion-study.py","asset_id":asset_id,"frames":brief['storyboard_beats'],"review_status":"pending-human-review"})


def scene_svg():
    pieces=[]
    for i,(x,y) in enumerate(SOURCE):
        pieces.append(f'<g id="{ID_PREFIX}{i+1:02d}" data-origin-slot="slot-{i+1:02d}"><circle cx="{x}" cy="{y}" r="39" fill="{PINK}"/><path d="M {x-10} {y-33} l -14 -20 l 27 5 Z" fill="#50795A"/></g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1080" viewBox="0 0 1440 1080">
<title>Provisional M01 editable schematic — pending human review</title>
<desc>Original vector layer map for the motion study. Five working occurrences plus a separate three-piece target model. Not selected app art.</desc>
<g id="environment-ground"><rect width="1440" height="1080" fill="{BG}"/></g>
<g id="target-reference" data-interactive="false"><rect x="505" y="180" width="430" height="140" rx="30" fill="#FFF0C9" stroke="{GOLD}" stroke-width="4"/><circle cx="620" cy="251" r="25" fill="{PINK}"/><circle cx="720" cy="251" r="25" fill="{PINK}"/><circle cx="820" cy="251" r="25" fill="{PINK}"/></g>
<g id="source-tray"><rect x="135" y="400" width="515" height="392" rx="45" fill="#E6D8BB"/></g>
<g id="basket-back"><rect x="790" y="400" width="540" height="405" rx="48" fill="#FAE8BF" stroke="#B7935C" stroke-width="5"/></g>
<g id="stationary-occurrences">{''.join(pieces)}</g>
<g id="basket-front"><rect x="786" y="770" width="548" height="35" rx="16" fill="#CCA76B"/></g>
<g id="moving-occurrence" data-instance-policy="move existing group here; never duplicate"/>
<g id="review-label"><text x="60" y="1000" fill="{INK}" font-size="24">PHASE 1 — PENDING HUMAN REVIEW — EDITABLE SCHEMATIC LAYER MAP</text></g>
</svg>'''


def encode(folder, reduced=False):
    label="reduced-motion" if reduced else "pickup-return-settle"
    with tempfile.TemporaryDirectory(prefix="mathbuddy-motion-") as tmp:
        td=Path(tmp)
        timeline=[]
        for frame in range(FRAMES):
            t=frame/FPS
            timeline.append({"frame":frame,**state_at(t,reduced)})
            render_m01(t,reduced).save(td/f"{frame:04d}.png")
        dump(folder/f"{label}-timeline.json",{"status":"provisional-pending-human-review","fps":FPS,"frame_count":FRAMES,"duration_seconds":DURATION,"silent":True,"reduced_motion":reduced,"semantic_inputs":[{"time_seconds":.72,"event":"accepted-move","id":ID_PREFIX+"03","to":"basket/slot-01"},{"time_seconds":2.88,"event":"accepted-return","id":ID_PREFIX+"03","to":"tray/slot-03"}],"frames":timeline})
        subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-framerate",str(FPS),"-i",str(td/"%04d.png"),"-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-movflags","+faststart",str(folder/f"{label}.mp4")],check=True)
        # The GIF is a smaller adult-review convenience, not a native export.
        subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",str(folder/f"{label}.mp4"),"-vf","fps=15,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse", "-loop","0",str(folder/f"{label}.gif")],check=True)


def decoded_quantity_check(path):
    """Count the actual berry silhouettes in every encoded frame.

    This is a technical color-component check of this controlled schematic,
    not proof of child comprehension or a reusable app asset validator.
    """
    import numpy as np
    from scipy import ndimage
    proc=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-i",str(path),"-f","rawvideo","-pix_fmt","rgb24","pipe:1"],stdout=subprocess.PIPE)
    count=[]
    frame_bytes=SIZE[0]*SIZE[1]*3
    while True:
        raw=proc.stdout.read(frame_bytes)
        if not raw:
            break
        if len(raw)!=frame_bytes:
            raise RuntimeError("Incomplete decoded RGB frame")
        pixels=np.frombuffer(raw,dtype=np.uint8).reshape(SIZE[1],SIZE[0],3).astype(np.int16)
        r,g,b=pixels[:,:,0],pixels[:,:,1],pixels[:,:,2]
        mask=(r>145)&(g<195)&(b>g+5)&(r>b+20)
        labels,n=ndimage.label(mask)
        sizes=np.bincount(labels.ravel())
        components=[i for i in range(1,n+1) if sizes[i]>500]
        centers=ndimage.center_of_mass(mask,labels,components)
        target_count=int(sum(y<320 for y,x in centers))
        working_count=int(sum(y>=320 for y,x in centers))
        count.append((target_count,working_count))
    proc.stdout.close()
    if proc.wait()!=0:
        raise RuntimeError("ffmpeg raw-frame decode failed")
    return {"path":str(path.relative_to(ROOT)),"actual_decoded_frames_examined":len(count),"method":"Red-berry connected components >500 px from actual decoded RGB frames; target centers above y=320, working centers below.","target_berry_count_min":min(x[0] for x in count),"target_berry_count_max":max(x[0] for x in count),"working_berry_count_min":min(x[1] for x in count),"working_berry_count_max":max(x[1] for x in count),"all_frames_have_reference_three_and_working_five":all(c==(3,5) for c in count),"limit":"Controlled schematic color-component measurement only; occurrence identity is checked separately against timeline data, and child understanding needs human review."}


def main():
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise RuntimeError("ffmpeg and ffprobe required for render/measurement")
    for asset_id,spec in SPECS.items():
        folder=OUT/asset_id
        folder.mkdir(parents=True,exist_ok=True)
        brief={**COMMON,"asset_id":asset_id,**spec,"coordinate_system":coordinate_contract(asset_id)}
        dump(folder/"brief.json",brief)
        if asset_id=="M01":
            frames=[render_m01(t) for t in [0,1.5,4.0]]
        else:
            fun={"M02":render_join,"M03":render_share,"M04":render_help,"M05":render_completion,"M06":render_garden,"M07":render_greeting}[asset_id]
            frames=[fun(i) for i in range(3)]
        storyboard(asset_id,frames,brief)
    m01=OUT/"M01"
    (m01/"scene-layers.svg").write_text(scene_svg())
    encode(m01)
    encode(m01,True)
    render_m01(1.5).save(m01/"poster.png")
    reduced=[render_m01(t,True) for t in [0,1.5,4.0]]
    redsheet=Image.new("RGB",(2160,540),BG)
    for i,frame in enumerate(reduced): redsheet.paste(frame.resize((720,540),Image.Resampling.LANCZOS),(720*i,0))
    redsheet.save(m01/"reduced-motion-contact-sheet.png")
    # Measurements examine the actual encoded outputs and all timeline frames.
    videos=[]
    for path in sorted(m01.glob("*.mp4")):
        result=subprocess.run(["ffprobe","-v","error","-count_frames","-show_streams","-show_format","-of","json",str(path)],capture_output=True,text=True,check=True)
        data=json.loads(result.stdout)
        stream=data["streams"][0]
        videos.append({"path":str(path.relative_to(ROOT)),"width":stream["width"],"height":stream["height"],"duration_seconds":float(data["format"]["duration"]),"decoded_frame_count":int(stream["nb_read_frames"]),"frame_rate":stream["r_frame_rate"],"audio_stream_count":sum(s["codec_type"]=="audio" for s in data["streams"]),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    # Decode actual encoded movie frames, rather than presenting only the source
    # drawing as evidence that the encoder succeeded.
    review=OUT/"review"
    key_frames=[0,27,34,45,90,102,120]
    select="select="+"+".join(f"eq(n\\,{n})" for n in key_frames)
    decoded_sheet=Image.new("RGB",(2240,710),BG)
    dd=ImageDraw.Draw(decoded_sheet)
    text(dd,(30,18),"ACTUAL DECODED MP4 FRAMES • NORMAL / REDUCED MOTION",30,bold=True)
    for row,name in enumerate(["pickup-return-settle","reduced-motion"]):
        folder=review/"decoded-frames"/name
        folder.mkdir(parents=True,exist_ok=True)
        subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",str(m01/f"{name}.mp4"),"-vf",select,"-vsync","0",str(folder/"frame-%02d.png")],check=True)
        for j,(path,n) in enumerate(zip(sorted(folder.glob("frame-*.png")),key_frames)):
            with Image.open(path) as f:
                decoded_sheet.paste(f.resize((320,240),Image.Resampling.LANCZOS),(320*j,90+row*300))
            text(dd,(320*j+10,339+row*300),f"{name}  {n/FPS:.2f}s",19)
    decoded_sheet.save(review/"decoded-key-frames.png")
    # Render each *actual PDF* back to pixels for page inspection.
    pdf_measurements=[]
    if shutil.which("pdftoppm"):
        pages=review/"pdf-pages"
        pages.mkdir(parents=True,exist_ok=True)
        allpdf=Image.new("RGB",(1800,2880),BG)
        ad=ImageDraw.Draw(allpdf)
        text(ad,(35,20),"ACTUAL STORYBOARD PDF PAGES • M01–M07 • PENDING HUMAN REVIEW",25,bold=True)
        for i,asset_id in enumerate(SPECS):
            pdf=OUT/asset_id/"storyboard.pdf"
            subprocess.run(["pdftoppm","-png","-singlefile","-scale-to-x","1200","-scale-to-y","900",str(pdf),str(pages/asset_id)],check=True,capture_output=True)
            with Image.open(pages/f"{asset_id}.png") as im:
                allpdf.paste(im.resize((900,675),Image.Resampling.LANCZOS),(900*(i%2),85+695*(i//2)))
                dims=list(im.size)
            # Each storyboard is a single-image, single-page PDF; confirm actual
            # page count using pypdf when installed, rather than assert a count.
            try:
                from pypdf import PdfReader
                pages_count=len(PdfReader(pdf).pages)
            except ImportError:
                pages_count=None
            pdf_measurements.append({"asset_id":asset_id,"path":str(pdf.relative_to(ROOT)),"actual_page_count":pages_count,"actual_pdf_raster_preview_px":dims,"preview":str((pages/f'{asset_id}.png').relative_to(ROOT))})
        allpdf.save(review/"all-storyboards-pdf-preview.png")
    geometry=[]
    for reduced in [False,True]:
        minimum_separation=float("inf")
        maximum_fruit_bottom=0
        target_card_clearance=float("inf")
        identity_ok=True
        for f in range(FRAMES):
            s=state_at(f/FPS,reduced)
            ids=[p['id'] for p in s['pieces']]
            identity_ok &= len(ids)==5 and len(set(ids))==5 and ids==[ID_PREFIX+f"{i+1:02d}" for i in range(5)]
            for i,p in enumerate(s['pieces']):
                maximum_fruit_bottom=max(maximum_fruit_bottom,p['center_px'][1]+39*p['scale'])
                if 505-39*p['scale'] <= p['center_px'][0] <= 935+39*p['scale']:
                    target_card_clearance=min(target_card_clearance,p['center_px'][1]-39*1.26*p['scale']-320)
                for q in s['pieces'][i+1:]:
                    a,b=p['center_px'],q['center_px']
                    distance=math.dist(a,b)-39*1.26*(p['scale']+q['scale'])
                    minimum_separation=min(minimum_separation,distance)
        geometry.append({"reduced_motion":reduced,"all_144_frames_have_exactly_five_unique_working_ids":identity_ok,"minimum_conservative_full_silhouette_gap_px":round(minimum_separation,2),"maximum_working_fruit_bottom_px":round(maximum_fruit_bottom,2),"basket_front_top_px":770,"minimum_rim_clearance_px":round(770-maximum_fruit_bottom,2),"minimum_given_card_clearance_px":round(target_card_clearance,2),"target_reference_count_all_frames":3,"target_reference_not_in_working_ids":True})
    validation={"status":"technical-measurements-complete-human-review-pending","scope":"Seven provisional contracts; M01 encoded study only; no final layer pack or native behavior verified","videos":videos,"actual_encoded_quantity_checks":[decoded_quantity_check(p) for p in sorted(m01.glob('*.mp4'))],"geometry":geometry,"pdfs":pdf_measurements,"actual_decoded_key_frame_review":str((review/'decoded-key-frames.png').relative_to(ROOT)),"human_decisions":{"art":"pending","motion_comfort":"pending","child_target_comprehension":"pending","final_character_identity":"pending","six_slot_final_layer_visibility":"pending","supported_family_iPad_actual_size_review":"pending"}}
    dump(OUT/"review/technical-measurements.json",validation)
    print(json.dumps(validation,indent=2))


if __name__ == "__main__":
    main()
