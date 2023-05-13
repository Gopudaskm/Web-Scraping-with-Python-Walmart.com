
This is a readme file that describes some errors or problems that were faced during the coding of a project or application.
 It contains important information that developers need to know to avoid similar errors or problems in the future.

Problem 1: Collecting required div from response tree element with appropriate xpath

When trying to collect the required div from the response tree element with the appropriate xpath (//div[@class="mb0 ph1 pa0-xl bb b--near-white w-25"]), 
only 10 div were collected instead of the expected 48 div. This was identified by comparing the output with the website as seen in  Screenshot(1).png 
and Screenshot (2).png. To solve this problem, the script in the response text with the xpath '//script[@id="__NEXT_DATA__"]//text()' was used to 
collect all product data. The text was converted to json format as seen in Screenshot (3).png.
This approach led to the collection of 52 data, out of which 4 were None values.

Problem 2: Getting None value after extracting product id

After extracting the product id, some None values were obtained as seen in Screenshot(4).png. To avoid the None values,
 an if statement was used to filter them out when updating the product id and product title to the dictionary as seen in Screenshot(5).png. 
This approach helped to avoid the None values and ensure that only valid data was processed.

Problem 3: SSLError or index out of range error

During the execution of the program, an SSLError or index out of range error could occur as seen in Screenshot(6).png and Screenshot(7).png. 
This is usually caused by the website blocking the current proxy. To solve this problem, a rotating proxy was used instead of the current proxy as seen in Screenshot(8).png. 
This approach helped to avoid the SSLError or index out of range error and ensure that the program was executed successfully.

In conclusion, the problems and errors faced during the coding of a project or application can be challenging. 
However, by documenting the solutions and sharing them in a readme file like this, developers can avoid similar errors 
in the future and ensure the successful execution of the project or application.