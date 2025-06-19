// Edit objectname and property and values

<?php
$objectname = [
    "property1" => "value1",
    "property2" => "value2"
];

// Serialize the array
$serialized = serialize($objectname);

// Output the serialized data
echo $serialized;
?>
