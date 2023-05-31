import xml.etree.cElementTree as ET

testsuites = ET.Element(
    "testsuites",
    name="FOCUS Validations",
    tests="3",
    failures="1",
    errors="0",
    skipped="1",
    assertions="3",
    time="0",
    timestamp="2021-04-02T15:48:23",
)

testsuite1 = ET.SubElement(testsuites, "testsuite", name="ColumnA", time="0.008")
testcase1 = ET.SubElement(testsuite1, "testcase", name="NotNull", time="0")
testcase2 = ET.SubElement(testsuite1, "testcase", name="UniqueValues", time="0")
ET.SubElement(
    testcase2,
    "failure",
    name="testCase2",
    message="Expected value did not match.",
    type="AssertionError",
).text = "Failed"
testcase3 = ET.SubElement(testsuite1, "testcase", name="Range", time="0.004")
ET.SubElement(testcase3, "skipped", message="Test was skipped.")

tree = ET.ElementTree(testsuites)
ET.indent(tree)
tree.write("reports/focus_validations.xml", encoding="utf-8", xml_declaration=True)
