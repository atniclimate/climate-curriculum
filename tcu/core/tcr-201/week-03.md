---
course: tcr-201
week: 3
title: Historic Records and Regional Projections
thread: "Module 2: Downscaling: From the Globe to the Reservation"
eyes: [bird]
sockets:
  - id: regional-signal
    purpose: "The regional climate science partners for {{region.name}} ({{region.casc}}, Extension, {{region.state_climatologist}}) as public sources, and the regional projection views captured from them as SNAPSHOT"
    eye: bird
    consent: C0
---
## Key lesson

Global models describe the planet in coarse boxes. Downscaling translates them to regional scales, using historic observations to correct and sharpen them. A projection is not a prediction; it asks: if the world follows this pathway, what range of climates is likely here?

## Key takeaway

Name the scenario, the period, the baseline, and the spread. A single number from a single model is a guess dressed up as a fact.

## Learning objectives

Students will be able to:

- Explain Shared Socioeconomic Pathways (SSPs) and describe SSP2-4.5 and SSP3-7.0, with the IPCC AR6 best-estimate warming for each.
- Distinguish statistical and dynamical downscaling, and explain bias correction and ensembles.
- Rebuild the historic temperature and precipitation record for the climate division or county that holds {{institution.town}}, or for the Nation or case they follow.
- Read regional projections for 2040 to 2069 and 2070 to 2099 under two scenarios, for their region, with the Pacific Northwest as the shared case.

## Before class

- SVS 5343, "NEX GDDP CMIP6 Historical and Predicted Global Maximum Monthly Temperature from 1950 - 2100" (09/23/2024; updated 10/28/2024): https://svs.gsfc.nasa.gov/5343
- IPCC AR6 Working Group I, Summary for Policymakers, Section B, "Possible Climate Futures."
- `[INSTRUCTOR SELECTS: one regional projection explainer from {{region.casc}}, Extension, or the {{region.state_climatologist}}]`
- Shared case: University of Washington Climate Impacts Group (CIG), Pacific Northwest Climate Projection Tool, background: https://cig.uw.edu/resources/analysis-tools/pacific-northwest-climate-projection-tool/ ; NCA5 Chapter 27, "Northwest," Key Messages: https://nca5.climate.us/ (volunteer-hosted copy) [verify]
- `[INSTRUCTOR SELECTS: the NCA5 regional chapter for {{region.name}}, Key Messages]` [verify]

The instructor, outside class, captures as dated SNAPSHOT files with meta.json:

- The NOAA NCEI Climate at a Glance annual temperature, summer (June to August) temperature, and annual precipitation series for the climate division or county that holds {{institution.town}} (https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/), where it covers your region [verify] (coverage outside the contiguous United States).
- The regional projection table for Lab 3B from the regional-signal socket, or from the case pack for {{place.climate_unit}}.
- The shared-case table from the CIG tool (East of the Cascades and West of the Cascades), so every site can run the shared-case row.

## Session shape

| Time | Module | What happens |
|---|---|---|
| 0 to 10 min | Presence | Check-in: what signal did you choose? |
| 10 to 30 min | Inquiry | Mini-lecture: from models to scenarios (Instructor notes). |
| 30 to 60 min | Inquiry | Mini-lecture: downscaling and how to read a projection. |
| 60 to 70 min | Presence | Break (split point). |
| 70 to 105 min | Application | Lab 3A: Rebuild the historic record, hand first. |
| 105 to 135 min | Application | Lab 3B: Read the regional projections, shared case and this region (Local lesson). |
| 135 to 150 min | Reflection | Debrief: history and future on one page; Check for Understanding; reflection. |

## Hands-on activity

Every view is a SNAPSHOT, labeled with source, issuer, capture date, and baseline; every projection view also names its scenario and period and says "projection, not a prediction." A blank is unknown, never zero.

**Lab 3A: Rebuild the historic record.**

1. **By hand first.** On the printed decade table for the division or county, plot decade averages of annual temperature on grid paper and lay a ruler along them for a trend. Hand twin: decade values read aloud and placed as sticky dots on a wall grid.
2. **On a spreadsheet.** Plot annual average temperature for the full record with a linear trend line; repeat for summer (June to August) temperature and annual precipitation. Record the page's baseline.
3. Optional: a smaller area from gridMET (https://www.climatologylab.org/gridmet.html) or PRISM (https://prism.oregonstate.edu/), where they cover your region [verify], from an instructor SNAPSHOT.
4. Look for: which season changed most; whether precipitation's year-to-year swing outweighs its trend; what a division average hides. A trend line describes the past, not the future.

**Lab 3B: Read the regional projections.**

1. **Shared case first (every site).** From the CIG SNAPSHOT: annual temperature change for East of the Cascades, CMIP6, 2050s (2040 to 2069), for SSP2-4.5 and SSP3-7.0; record each scenario's range and middle. Repeat for the 2080s (2070 to 2099), summer, and precipitation, and one row for West of the Cascades, with baseline, source, and date. The CIG tool reports change against its own historical baseline (1950 to 1999) [verify], a third baseline; confirm both scenarios are selectable [verify].
2. **This region.** Fill the same table from the regional SNAPSHOT (Local lesson). If no regional source names both scenarios, record which scenarios it does name and mark the missing cells unknown.
3. Ask: do the scenarios differ more at mid-century or end of century, and why? How does projected change compare with the historic change you plotted?
4. Alternates where they cover your region: LOCA2 (https://loca.ucsd.edu/), used for the Fifth National Climate Assessment, with SSP2-4.5 and SSP3-7.0 datasets listed on NOAA's Climate Resilience Information System (https://cris.climate.gov) [verify] (availability and coverage); The Climate Toolbox (https://climatetoolbox.org/), whose projection pages the source course found to use CMIP5, not CMIP6 [verify].

| Row | Scenario | 2040 to 2069 (range; middle) | 2070 to 2099 (range; middle) | Baseline | Source and capture date |
|---|---|---|---|---|---|
| Shared case: East of the Cascades, annual temperature | SSP2-4.5 | | | | |
| Shared case: East of the Cascades, annual temperature | SSP3-7.0 | | | | |
| This region, annual temperature | SSP2-4.5 | | | | |
| This region, annual temperature | SSP3-7.0 | | | | |

**More than one way in:** read the table aloud, mark the range with two hands apart, or sketch two arrows from today. **No internet:** the lab runs from the printed tables.

## Local lesson

**Shared case: {{case.shared}}.** The Pacific Northwest projections (CIG tool) are the worked regional example every site runs, so classes across the country can compare notes.

**This region: {{region.name}}.** The regional climate science partners publish their own projections and explainers. The regional SNAPSHOT for Lab 3B comes from them or from the case pack for {{place.climate_unit}}.

{{socket:tcr-201/week-03/regional-signal}}

Room for: the regional science partners near {{institution.name}} ({{region.casc}}, Extension, the {{region.state_climatologist}}), named from their own public pages, the regional projection table they publish, and the faculty who read it with students. [LOCAL EXPERT: TCU faculty or knowledge holder]

## Check for Understanding

1. A classmate says "SSP3-7.0 is what will happen." What would you say back? Say it, or draw two paths from today.
   Listen for: a scenario is an "if," not a forecast; both scenarios are possible; choices still being made separate them.
2. What is the difference between statistical and dynamical downscaling, in one sentence each?
   Listen for: statistical uses observed relationships between local climate and model output, fast, many models; dynamical runs a regional model inside a global one, detailed, costly, fewer models.
3. Your table has a range and a middle. Why not report only the one model you like best?
   Listen for: the ensemble range shows uncertainty from models, scenarios, and natural swings; one model's number hides that.

## Assignment

**Regional signal worksheet:** the Lab 3B table (shared-case rows and this region's rows) plus one paragraph comparing the historic record with the projections for your signal, with scenario, period, baseline, source, and date named. It becomes the regional section of your Signal Brief.

## Reflection

1. What did you learn about how a global projection becomes a regional one?
2. What idea about "the future climate" shifted when you saw a range instead of a number?
3. What one question about the scenarios will you carry forward?

**Say it plain:** Scientists bring the world's climate models down to our region and give a range of futures for each choice people make; we always say which choice, which years, and compared to what.

## Guest or Elder slot

`[PLACEHOLDER: a scientist from {{region.casc}}, Extension, the {{region.state_climatologist}}, or a TCU scientist who works with downscaled data alongside Tribes, invited and compensated, speaking as themselves]` Shared case: the source course invited a Climate Impacts Group or NW CASC scientist.

[LOCAL EXPERT: TCU faculty or knowledge holder]

## Instructor notes

- **Mini-lecture: from models to scenarios.** SSPs pair a story of how the world develops with a level of greenhouse gas forcing by 2100. IPCC AR6 best-estimate warming for 2081 to 2100, compared with 1850 to 1900: SSP1-2.6 about 1.8 °C (3.2 °F); SSP2-4.5 about 2.7 °C (4.9 °F); SSP3-7.0 about 3.6 °C (6.5 °F); SSP5-8.5 about 4.4 °C (7.9 °F). SSP2-4.5 is a middle-of-the-road pathway; SSP3-7.0 is a high-emissions, fragmented-world pathway. SVS 5343 shows global maximum monthly temperature from 1950 to 2100 under four SSPs from the NASA Earth Exchange Global Daily Downscaled Projections (NEX-GDDP-CMIP6), a bias-corrected, downscaled version of the Coupled Model Intercomparison Project Phase 6 (CMIP6) models; the same dataset underlies the Week 4 Tribal-scale projections.
- **Downscaling.** Statistical downscaling (NEX-GDDP-CMIP6 and Localized Constructed Analogs version 2, LOCA2, are statistical) uses relationships between observed local climate and model output. Dynamical downscaling runs a regional climate model inside a global one. Bias correction adjusts model output so its historic period matches observations. Report the range and middle across models, never a favorite. NEX-GDDP-CMIP6 cells are 0.25 degree, roughly 25 kilometers; gridMET (Climatology Lab) is about 4 kilometers, daily, from 1979; PRISM (Oregon State University) offers 4 kilometer and 800 meter grids, monthly back to 1895. Write the baseline down every time.
- Students often ask which scenario is "right." Neither. Scenarios are "if" statements. The honest answer names both and says what separates them: choices still being made.
- Regional tools cover different areas and different scenario generations; never assert that a tool covers this region until you have opened it for this region and recorded the date.
- Data posture: Climate at a Glance, CIG, LOCA2, and the Toolbox are LIVE sites the instructor opens outside class; the class works from dated SNAPSHOT tables.

## Sovereignty thread

Reading a projection honestly (scenario, period, baseline, spread) is how a Nation keeps someone else's single number from setting its priorities (Ring 1: The Nation). Regional science partners and InterTribal networks share these readings across Nations (Ring 2: InterTribal), and the scenarios themselves come from the international assessment (Ring 3: International).
