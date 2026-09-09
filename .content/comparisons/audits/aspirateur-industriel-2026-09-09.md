# AUDIT — `/comparatifs/aspirateur-industriel/`

Date: 2026-09-09
Mode: `AUDIT`
Decision: `DEEP_REWRITE`
Confidence: 99%
Indexing: `KEEP_NOINDEX`

## Intent

The URL can be valuable, but the current page does not serve the industrial-vacuum universe accurately enough.

## Preserve

- the attempt to distinguish industrial from ordinary professional use;
- capacity, duty cycle, handling and dust-safety as decision dimensions;
- the existing warning that fixed/process/ATEX systems are a different universe.

## Blockers

1. **The product universe contradicts the stated boundary.** The page compares Kärcher NT 50/1, NT 30/1 and Bosch GAS 35 M AFC — professional wet/dry/safety vacuums — while current industrial ranges include dedicated IVC/IVR-type machines, process-duty equipment, mobile/stationary solutions and ATEX variants.
2. **`Industrial = large capacity` is too narrow.** The hub label reduces the intent to tank size, while true industrial selection also depends on duty cycle, motor technology, discharge system, material, explosive atmosphere and process integration.
3. **The page overlaps heavily with class M and professional.** Two of its three products are also core candidates in the class-M/general legacy pages.
4. **The current score treats class M as a generic industrial quality factor.** Industrial vacuuming can involve L/M/H, ATEX/ACD, liquids, chips, process dust or other requirements; class M is not the definition of the category.
5. **Legacy cloned architecture** masks the need for a fundamentally different candidate taxonomy.

## Current market evidence

Kärcher's current industrial-vacuum taxonomy separates industrial vacuuming from standard NT wet/dry machines and includes mobile/stationary, continuous/process and ATEX solutions.

References checked 2026-09-09:
- https://www.kaercher.com/fr/professional/aspirateurs-industriels.html
- https://www.kaercher.com/be-fr/professional/solutions-industrielles-aspiration-et-depoussierage/aspirateurs-industriels/aspirateurs-industriels-solides-poussieres/ivc-60-24-2-tact2-m-15761050.html
- https://www.kaercher.com/be-fr/professional/solutions-industrielles-aspiration-et-depoussierage/aspirateurs-industriels/aspirateurs-industriels-solides-poussieres/ivr-60-30-sc-m-acd-99906430.html

## Missing data

- the site does not yet have a persisted industrial candidate universe;
- no decision has been documented on whether the site's editorial scope should extend to true process/industrial machines;
- GSC/semantic value for the industrial query was not available in this audit.

## Next step

Before writing anything, decide scope:

A. if `industrial` is strategically in scope, research a real industrial candidate universe and rebuild from duty/application categories;
B. if the site only wants portable construction wet/dry vacuums, keep this URL noindex and consider a later MERGE into professional rather than publishing a misleading industrial page.

Current recommendation remains `DEEP_REWRITE`, not indexation.
