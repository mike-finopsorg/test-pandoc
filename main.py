import xml.etree.cElementTree as ET

testsuites = ET.Element("testsuites")

testsuite1 = ET.SubElement(
    testsuites, "testsuite", name="Tests.Registration", time="0.008"
)
testcase1 = ET.SubElement(testsuite1, "testcase", name="testCase1", time="0.004")
testcase2 = ET.SubElement(testsuite1, "testcase", name="testCase2", time="0.004")
ET.SubElement(
    testsuite1,
    "failure",
    name="testCase2",
    message="Expected value did not match.",
    type="AssertionError",
)


tree = ET.ElementTree(testsuites)
ET.indent(tree)
tree.write("reports/focus_validations.xml", encoding="utf-8", xml_declaration=True)
