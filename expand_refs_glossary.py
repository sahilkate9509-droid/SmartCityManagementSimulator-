with open('content_chapters_6_8.py', 'r', encoding='utf-8') as f:
    text = f.read()

more_refs = '''        "[30] F. A. Gifford, \\"Turbulent Diffusion-Typing Schemes: A Review,\\" <i>Nuclear Safety</i>, vol. 17, no. 1, pp. 68-86, 1976.",
        "[31] M. Wegener, \\"Operational Urban Models: State of the Art,\\" <i>Journal of the American Planning Association</i>, vol. 60, no. 1, pp. 17-29, 1994.",
        "[32] H. A. Simon, <i>The Sciences of the Artificial</i>, 3rd ed. Cambridge, MA: MIT Press, 1996.",
        "[33] P. M. Torrens, \\"Cellular Automata and Multi-Agent Systems as Theoretical and Practical Tools for Urban Modeling,\\" <i>Environment and Planning B: Planning and Design</i>, vol. 33, no. 2, pp. 245-265, 2006.",
        "[34] D. C. Montgomery, <i>Design and Analysis of Experiments</i>, 10th ed. Hoboken, NJ: John Wiley & Sons, 2020.",
        "[35] W. R. Ashby, <i>An Introduction to Cybernetics</i>. London: Chapman & Hall, 1956.",
        "[36] T. C. Schelling, <i>Micromotives and Macrobehavior</i>. New York: W. W. Norton & Company, 1978.",
        "[37] E. Ostrom, <i>Governing the Commons: The Evolution of Institutions for Collective Action</i>. Cambridge: Cambridge University Press, 1990.",
        "[38] D. L. Meadows, J. Randers, and W. W. Behrens, <i>The Limits to Growth</i>. New York: Universe Books, 1972.",
        "[39] K. Lynch, <i>The Image of the City</i>. Cambridge, MA: MIT Press, 1960.",
        "[40] J. Jacobs, <i>The Death and Life of Great American Cities</i>. New York: Random House, 1961."'''

target_r30 = '"[30] F. A. Gifford, \\"Turbulent Diffusion-Typing Schemes: A Review,\\" <i>Nuclear Safety</i>, vol. 17, no. 1, pp. 68-86, 1976."'
if target_r30 in text:
    text = text.replace(target_r30, more_refs, 1)

more_glossary = '''        [Paragraph("<b>Volume-to-Capacity (V/C) Ratio</b>", styles['TableCellBold']), Paragraph("A standard transportation engineering measure of traffic congestion comparing actual vehicular traffic volume to the theoretical maximum flow rate.", styles['TableCell'])],
        [Paragraph("<b>Cellular Automata (CA)</b>", styles['TableCellBold']), Paragraph("A discrete mathematical spatial model consisting of a regular grid of cells, each in one of a finite number of states that evolve synchronously according to local transition rules.", styles['TableCell'])],
        [Paragraph("<b>Multi-Criteria Decision Analysis (MCDA)</b>", styles['TableCellBold']), Paragraph("A sub-discipline of operations research evaluating multiple conflicting criteria in decision making, used here for Composite Smart City Index normalization.", styles['TableCell'])],
        [Paragraph("<b>Level of Detail (LOD)</b>", styles['TableCellBold']), Paragraph("A computer graphics technique decreasing 3D mesh complexity as distances from the viewer increase, reducing vertex load and preserving GPU fill-rate.", styles['TableCell'])],
        [Paragraph("<b>B-Tree Index</b>", styles['TableCellBold']), Paragraph("A self-balancing search tree data structure maintaining sorted keys for logarithmic O(log N) lookup, insertion, and sequential range query access in databases.", styles['TableCell'])],
        [Paragraph("<b>Multi-Version Concurrency Control (MVCC)</b>", styles['TableCellBold']), Paragraph("A database concurrency management paradigm where transactions see point-in-time snapshots of data, enabling readers and writers to operate without mutual blocking.", styles['TableCell'])],
        [Paragraph("<b>Generational Garbage Collection</b>", styles['TableCellBold']), Paragraph("A runtime memory optimization heuristic segregating objects into age generations (Gen 0, Gen 1, Gen 2) based on the observation that young objects die quickly.", styles['TableCell'])],
        [Paragraph("<b>Pasquill-Gifford Stability Classes</b>", styles['TableCellBold']), Paragraph("A standard meteorological classification system (Classes A to F) characterizing atmospheric turbulence and dispersion potential for plume emission modeling.", styles['TableCell'])],
        [Paragraph("<b>Webster's Traffic Delay Formula</b>", styles['TableCellBold']), Paragraph("A classic empirical transportation formula computing vehicular queue delays at signalized road intersections as a function of cycle time and green light ratios.", styles['TableCell'])],
        [Paragraph("<b>Data Transfer Object (DTO)</b>", styles['TableCellBold']), Paragraph("An object carrying data between software processes or network boundaries without containing business domain logic, used for FastAPI serialization.", styles['TableCell'])],
        [Paragraph("<b>Swagger UI / OpenAPI</b>", styles['TableCellBold']), Paragraph("An open-source software framework facilitating interactive browser-based visualization and testing of RESTful API endpoints without dedicated client applications.", styles['TableCell'])],'''

target_g_end = "[Paragraph(\"<b>Volume-to-Capacity (V/C) Ratio</b>\", styles['TableCellBold']), Paragraph(\"A standard transportation engineering measure of traffic congestion comparing actual vehicular traffic volume to the theoretical maximum flow rate.\", styles['TableCell'])],"
if target_g_end in text:
    text = text.replace(target_g_end, more_glossary, 1)

with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated references to 40 and glossary to 30 items.")
