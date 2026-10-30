## Practical 1: Creation of Test Suite Using Selenium IDE

Aim:\
To create and execute a Selenium IDE test suite containing four test cases to validate HTML, XML, JSON, and dynamic form pages, and export the automation script in WebDriver format.

Code – Selenium IDE commands

Create four test cases in Selenium IDE:

TC01_HTML

| Command    | Target            | Value                                |
| ---------- | ----------------- | ------------------------------------ |
| open       | `/test_html.html` |                                      |
| type       | `id=studentName`  | Karan                                |
| type       | `id=email`        | test\@gmail.com                      |
| click      | `id=submitBtn`    |                                      |
| assertText | `id=result`       | HTML Test Successful - Welcome Karan |

TC02_XML

| Command              | Target           | Value |
| -------------------- | ---------------- | ----- |
| open                 | `/test_data.xml` |       |
| assertElementPresent | `css=body`       |       |

TC03_JSON

| Command              | Target            | Value |
| -------------------- | ----------------- | ----- |
| open                 | `/test_data.json` |       |
| assertElementPresent | `css=body`        |       |

TC04_Dynamic_Form

| Command | Target                   | Value                         |
| ------- | ------------------------ | ----------------------------- |
| open    | `/dynamic_form.html`     |                               |
| type    | `id=studentName`         | Karan                         |
| select  | `id=course`              | `label=B.Sc Computer Science` |
| type    | `id=programmingLanguage` | C++                           |
| click   | `id=submitBtn`           |                               |




## Practical 2: Cross-Website Functional Testing Using Selenium IDE

Aim:\
To develop and execute a Selenium IDE test suite for two different web pages and perform cross-website functional testing by navigating between the pages and validating their functionality.

Code – Selenium IDE commands

| Command    | Target           | Value                           |
| ---------- | ---------------- | ------------------------------- |
| open       | `/site1.html`    |                                 |
| click      | `id=site2Link`   |                                 |
| type       | `id=studentName` | Karan                           |
| click      | `id=submitBtn`   |                                 |
| assertText | `id=result`      | Welcome Karan - Test Successful |




## Practical 3: Manual Test Case Design and Execution

Aim:\
To design, document, and manually execute test cases for a login web application using a Test Plan, Test Scenarios, Test Cases, Test Execution Report, and Defect Report.

Code – `manual_login.html`

```
<!DOCTYPE html>
<html>
<head>
    <title>STQA Manual Testing</title>
</head>
<body>

<h1>Student Login</h1>

<label>Username:</label>
<input type="text" id="username">

<br><br>

<label>Password:</label>
<input type="password" id="password">

<br><br>

<button id="loginBtn" onclick="login()">Login</button>

<p id="result"></p>

<script>
function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (username === "" && password === "") {
        document.getElementById("result").innerText =
            "Username and Password are required";
    }
    else if (username === "") {
        document.getElementById("result").innerText =
            "Username is required";
    }
    else if (password === "") {
        document.getElementById("result").innerText =
            "Password is required";
    }
    else if (username === "Admin" && password === "admin123") {
        document.getElementById("result").innerText =
            "Login Successful";
    }
    else {
        document.getElementById("result").innerText =
            "Invalid Username or Password";
    }
}
</script>

</body>
</html>
```




## Practical 4: Selenium Server (Grid) Configuration and Remote Execution

Aim:\
To install and configure Selenium Server in Hub-Node architecture, execute a test script on multiple browsers using Remote WebDriver, and compare cross-browser results.

Code – `multi_browser_test.py`

```
from selenium import webdriverfrom selenium.webdriver.common.by import ByURL = "http://localhost:8000/manual_login.html"def run_test(browser):    options = None    if browser == "chrome":        options = webdriver.ChromeOptions()    elif browser == "edge":        options = webdriver.EdgeOptions()    elif browser == "firefox":        options = webdriver.FirefoxOptions()    driver = webdriver.Remote(        command_executor="http://localhost:4444",        options=options    )    driver.get(URL)    driver.find_element(By.ID, "username").send_keys("Admin")    driver.find_element(By.ID, "password").send_keys("admin123")    driver.find_element(By.ID, "loginBtn").click()    result = driver.find_element(By.ID, "result").text    print(browser, ":", result)    driver.quit()for browser in ["chrome", "edge", "firefox"]:    run_test(browser)
```




## Practical 5: Login Automation and Validation

Aim:\
To write an automation script to perform login on a specified web page and verify successful login using URL validation, welcome message validation, and logout visibility check.

Code – `LoginTest.java`

```
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;

public class LoginTest {

    public static void main(String[] args) {

        WebDriver driver = new EdgeDriver();

        driver.get(
            "http://localhost:8000/login_automation.html"
        );

        driver.findElement(By.id("username"))
              .sendKeys("Admin");

        driver.findElement(By.id("password"))
              .sendKeys("admin123");

        driver.findElement(By.id("loginBtn"))
              .click();

        // URL Validation
        assert driver.getCurrentUrl().contains("dashboard.html");
        System.out.println("URL Validation: PASS");

        // Welcome Message Validation
        String welcome =
            driver.findElement(By.id("welcome")).getText();

        assert welcome.equals("Welcome Admin");
        System.out.println("Welcome Message Validation: PASS");

        // Logout Visibility Validation
        WebElement logoutButton =
            driver.findElement(By.id("logoutBtn"));

        assert logoutButton.isDisplayed();
        System.out.println("Logout Visibility Validation: PASS");

        System.out.println("Login Automation Test: PASSED");

        driver.quit();
    }
}
```



## Practical 6: Web Element Interaction and Synchronization Handling

Aim: Develop a Selenium WebDriver script to interact with textbox, radio button, checkbox, dropdown, alert, and frames. Implement implicit and explicit waits.

Code – `WebElementsTest.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.support.ui.*;
import java.time.Duration;

public class WebElementsTest {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.manage().timeouts()
              .implicitlyWait(Duration.ofSeconds(5));

        driver.get("http://localhost:8000/web_elements.html");

        driver.findElement(By.id("studentName"))
              .sendKeys("Krish");

        driver.findElement(By.id("male")).click();
        driver.findElement(By.id("agree")).click();

        Select course = new Select(
            driver.findElement(By.id("course")));
        course.selectByVisibleText("B.Sc Computer Science");

        driver.findElement(By.id("alertBtn")).click();
        Alert alert = driver.switchTo().alert();
        System.out.println(alert.getText());
        alert.accept();

        driver.switchTo().frame(
            driver.findElement(By.id("studentFrame")));
        driver.findElement(By.id("frameInput"))
              .sendKeys("Krish");

        driver.switchTo().defaultContent();

        driver.findElement(By.id("submitBtn")).click();

        WebDriverWait wait = new WebDriverWait(
            driver, Duration.ofSeconds(5));

        WebElement result = wait.until(
            ExpectedConditions.visibilityOfElementLocated(
                By.id("result")));

        System.out.println(result.getText());
        driver.quit();
    }
}
```




## Practical 7: Data-Driven Testing Using Excel Integration

Aim: Write a program to update 10 student records in an Excel file and validate changes on the web application using Apache POI.

Code – `StudentDataTest.java`

```
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import java.io.*;

public class StudentDataTest {
    public static void main(String[] args) throws Exception {

        String file = "student_data.xlsx";
        int[] marks = {90, 83, 95, 80, 75, 88, 72, 79, 94, 85};

        FileInputStream input = new FileInputStream(file);
        Workbook workbook = new XSSFWorkbook(input);
        Sheet sheet = workbook.getSheetAt(0);

        input.close();

        for (int i = 1; i <= 10; i++) {
            Row row = sheet.getRow(i);
            row.getCell(3).setCellValue(marks[i - 1]);
        }

        FileOutputStream output = new FileOutputStream(file);
        workbook.write(output);
        output.close();
        workbook.close();

        WebDriver driver = new EdgeDriver();
        driver.get("http://localhost:8000/student_records.html");

        for (int i = 1; i <= 10; i++) {
            driver.findElement(By.id("marks" + (100 + i)))
                  .clear();
            driver.findElement(By.id("marks" + (100 + i)))
                  .sendKeys(String.valueOf(marks[i - 1]));
        }

        driver.findElement(By.id("updateBtn")).click();

        System.out.println(
            driver.findElement(By.id("result")).getText());

        driver.quit();
    }
}
```




## Practical 8: Data Extraction and Score Analysis from Web Table

Aim: Automate extraction of student marks from a dynamic web table and calculate the number and percentage of students scoring above 60 in at least one subject.

Code – `TableAnalysis.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import java.util.*;

public class TableAnalysis {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.get("http://localhost:8000/student_marks.html");

        List<WebElement> rows =
            driver.findElements(By.cssSelector("#marksTable tr"));

        int count = 0;
        int total = rows.size() - 1;

        for (int i = 1; i < rows.size(); i++) {
            List<WebElement> cells =
                rows.get(i).findElements(By.tagName("td"));

            int m1 = Integer.parseInt(cells.get(2).getText());
            int m2 = Integer.parseInt(cells.get(3).getText());
            int m3 = Integer.parseInt(cells.get(4).getText());

            if (m1 > 60 || m2 > 60 || m3 > 60) {
                count++;
            }
        }

        double percentage = (count * 100.0) / total;

        System.out.println("Students above 60: " + count);
        System.out.println("Percentage: " + percentage + "%");

        driver.quit();
    }
}
```




## Practical 9: Object Identification and Counting on Web Page

Aim: Identify and count different web elements on a web page using Selenium WebDriver.

Code – `ObjectCount.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;

public class ObjectCount {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.get("http://localhost:8000/objects.html");

        System.out.println("Textboxes: " +
            driver.findElements(By.tagName("input")).size());

        System.out.println("Buttons: " +
            driver.findElements(By.tagName("button")).size());

        System.out.println("Links: " +
            driver.findElements(By.tagName("a")).size());

        System.out.println("Images: " +
            driver.findElements(By.tagName("img")).size());

        System.out.println("Dropdowns: " +
            driver.findElements(By.tagName("select")).size());

        driver.quit();
    }
}
```




## Practical 10: List and Combo Box Item Verification

Aim: Verify the items present in list boxes and combo boxes using Selenium WebDriver.

Code – `ListVerification.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.support.ui.Select;
import java.util.List;

public class ListVerification {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.get("http://localhost:8000/list.html");

        Select dropdown = new Select(
            driver.findElement(By.id("course")));

        List<WebElement> options = dropdown.getOptions();

        for (WebElement option : options) {
            System.out.println(option.getText());
        }

        dropdown.selectByVisibleText("B.Sc Computer Science");

        System.out.println("Selected: " +
            dropdown.getFirstSelectedOption().getText());

        driver.quit();
    }
}
```




## Practical 11: Checkbox Identification and Validation

Aim: Identify checkboxes on a web page, verify their selection status, and perform checkbox operations using Selenium WebDriver.

Code – `CheckboxTest.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import java.util.List;

public class CheckboxTest {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.get("http://localhost:8000/checkbox.html");

        List<WebElement> boxes =
            driver.findElements(By.cssSelector(
                "input[type='checkbox']"));

        System.out.println("Total Checkboxes: " + boxes.size());

        for (WebElement box : boxes) {
            if (!box.isSelected()) {
                box.click();
            }
        }

        for (WebElement box : boxes) {
            System.out.println("Selected: " + box.isSelected());
        }

        driver.quit();
    }
}
```




## Practical 12: Dynamic Web Table Handling and Sorting Validation

Aim: Handle dynamic web tables, extract table data, and validate sorting functionality using Selenium WebDriver.

Code – `DynamicTableTest.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import java.util.*;

public class DynamicTableTest {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.get("http://localhost:8000/dynamic_table.html");

        driver.findElement(By.id("sortBtn")).click();

        List<WebElement> rows =
            driver.findElements(By.cssSelector("#studentTable tr"));

        String previous = "";

        for (int i = 1; i < rows.size(); i++) {
            String name = rows.get(i)
                .findElements(By.tagName("td"))
                .get(1).getText();

            System.out.println(name);

            if (name.compareToIgnoreCase(previous) < 0) {
                System.out.println("Sorting Failed");
                driver.quit();
                return;
            }

            previous = name;
        }

        System.out.println("Sorting Passed");
        driver.quit();
    }
}
```




## Practical 13: File Upload and Download Automation

Aim: Develop a script to automate file upload and download functionality. Validate successful upload and verify file existence after download.

Code – `FileTest.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import java.io.File;

public class FileTest {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.get("http://localhost:8000/file_upload.html");

        // Upload file
        WebElement upload = driver.findElement(By.id("fileUpload"));
        upload.sendKeys("C:\\STQA\\sample.txt");

        driver.findElement(By.id("uploadBtn")).click();

        System.out.println(
            driver.findElement(By.id("result")).getText());

        // Download file
        driver.findElement(By.id("downloadBtn")).click();

        driver.quit();
    }
}
```




## Practical 14: Screenshot Capture and Logging Mechanism

Aim: Implement screenshot capture on test failure and integrate a logging mechanism using Log4j. Generate execution logs and analyze error messages.

Code – `ScreenshotTest.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import java.io.File;
import org.openqa.selenium.io.FileHandler;

public class ScreenshotTest {

    static Logger log = LogManager.getLogger(
        ScreenshotTest.class);

    public static void main(String[] args) throws Exception {
        WebDriver driver = new EdgeDriver();

        try {
            driver.get("http://localhost:8000/login.html");

            driver.findElement(By.id("username"))
                  .sendKeys("Krish");

            driver.findElement(By.id("loginBtn")).click();

            log.info("Test executed successfully");

        } catch (Exception e) {
            log.error("Test failed", e);

            File src = ((TakesScreenshot) driver)
                .getScreenshotAs(OutputType.FILE);

            FileHandler.copy(src,
                new File("failure.png"));

        } finally {
            driver.quit();
        }
    }
}
```




## Practical 15: Page Object Model (POM) Framework Implementation

Aim: Design and implement an automation framework using Page Object Model. Create reusable page classes and execute modular test cases.

Code – `LoginPage.java`

```
import org.openqa.selenium.*;

public class LoginPage {
    WebDriver driver;

    By username = By.id("username");
    By password = By.id("password");
    By loginBtn = By.id("loginBtn");

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    public void login(String user, String pass) {
        driver.findElement(username).sendKeys(user);
        driver.findElement(password).sendKeys(pass);
        driver.findElement(loginBtn).click();
    }
}
```

Code – `LoginTest.java`

```
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;

public class LoginTest {
    public static void main(String[] args) {
        WebDriver driver = new EdgeDriver();

        driver.get("http://localhost:8000/login.html");

        LoginPage page = new LoginPage(driver);
        page.login("Admin", "admin123");

        System.out.println("Login Test Executed");

        driver.quit();
    }
}
```




## Practical 16: TestNG Framework Implementation and Reporting

Aim: Create and execute automated test cases using TestNG annotations. Group test cases, define priorities, and generate HTML test reports.

Code – `TestNGTest.java`

```
import org.testng.annotations.*;
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import org.testng.Assert;

public class TestNGTest {

    WebDriver driver;

    @BeforeClass
    public void setup() {
        driver = new EdgeDriver();
        driver.get("http://localhost:8000/login.html");
    }

    @Test(priority = 1, groups = {"login"})
    public void titleTest() {
        Assert.assertTrue(
            driver.getTitle().contains("Login"));
    }

    @Test(priority = 2, groups = {"login"})
    public void loginTest() {
        driver.findElement(By.id("username"))
              .sendKeys("Admin");

        driver.findElement(By.id("password"))
              .sendKeys("admin123");

        driver.findElement(By.id("loginBtn")).click();

        Assert.assertTrue(
            driver.getCurrentUrl().contains("dashboard"));
    }

    @AfterClass
    public void close() {
        driver.quit();
    }
}
```




## Practical 17: Continuous Integration Using Jenkins

Aim: Configure Jenkins to execute Selenium automation scripts automatically. Generate build reports and analyze test execution history.

Code – Jenkins Build Commands

```
cd C:\STQA\Prac17

javac -cp ".;C:\selenium\selenium-server-4.49.0.jar" LoginTest.java

java -cp ".;C:\selenium\selenium-server-4.49.0.jar" LoginTest
```

Jenkins Configuration:

1. Open Jenkins at `http://localhost:8080`.
2. Create a new Freestyle Project.
3. Open Build Steps → Execute Windows batch command.
4. Enter the above commands.
5. Click Save → Build Now.
6. Check Console Output and Build History.




## Practical 18: Cross-Browser Testing Using Selenium Grid

Aim: Execute automation scripts across multiple browsers (Chrome, Firefox, Edge) using Selenium Grid. Compare execution time and compatibility issues.

Code – `CrossBrowserTest.py`

```
from selenium import webdriverfrom selenium.webdriver.common.by import Byimport timebrowsers = ["chrome", "firefox", "MicrosoftEdge"]for browser in browsers:    options = None    if browser == "chrome":        options = webdriver.ChromeOptions()    elif browser == "firefox":        options = webdriver.FirefoxOptions()    else:        options = webdriver.EdgeOptions()    start = time.time()    driver = webdriver.Remote(        command_executor="http://localhost:4444",        options=options    )    driver.get("http://localhost:8000/login.html")    print(browser, driver.title)    print("Execution Time:", time.time() - start)    driver.quit()
```




## Practical 19: Load Testing Using Apache JMeter

Aim: Design and execute load testing scenarios for a web application. Configure thread groups, ramp-up time, and loop count. Analyse response time, throughput, and error percentage using graphical reports.

Configuration – JMeter

1. Open Apache JMeter.
2. Add Test Plan → Thread Group.
3. Set the following values:

| Setting                   | Value     |
| ------------------------- | --------- |
| Number of Threads (Users) | 10        |
| Ramp-Up Period            | 5 seconds |
| Loop Count                | 2         |

4. Add Sampler → HTTP Request.
5. Configure:

```
Server Name: localhost
Port Number: 8000
Method: GET
Path: /index.html
```

6. Add listeners:
   - Summary Report
   - View Results Tree
   - Graph Results
7. Click Start to execute the load test.

Result: Response time, throughput, and error percentage are displayed in the JMeter reports.




## Practical 20: Bug Tracking and Defect Lifecycle Management

Aim: Log software defects using Bugzilla, assign severity and priority levels, track defect lifecycle stages, and generate defect summary reports.

Code – `buggy_login.html`

```
<!DOCTYPE html>
<html>
<head>
    <title>Student Portal Login</title>
</head>
<body>

<h1>Student Portal Login</h1>

<label>Username:</label>
<input type="text" id="username">

<br><br>

<label>Password:</label>
<input type="password" id="password">

<br><br>

<button id="loginBtn" onclick="loginUser()">Login</button>
<button id="resetBtn" onclick="resetForm()">Reset</button>

<p id="result"></p>

<script>
function loginUser() {
    let user = document.getElementById("username").value;

    // BUG-101: Password validation is missing
    if (user === "Krish") {
        document.getElementById("result").innerText =
            "Login Successful - Welcome " + user;
    } else {
        document.getElementById("result").innerText =
            "Invalid Username or Password";
    }
}

function resetForm() {
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";

    // BUG-102: Result message is not cleared
}
</script>

</body>
</html>
```

Bugzilla Configuration:

1\. Start the local web server:

```
py -m http.server
```

2\. Open the application:

```
http://localhost:8000/buggy_login.html
```

3\. Open Bugzilla:

```
http://localhost/bugzilla/enter_bug.cgi
```

4\. Report defects with severity and priority:

| Bug ID  | Defect                              | Severity | Priority |
| ------- | ----------------------------------- | -------- | -------- |
| BUG-101 | Login succeeds with blank password  | Critical | P1       |
| BUG-102 | Reset does not clear result message | Major    | P2       |
| BUG-103 | Email accepts address without @     | Normal   | P2       |
| BUG-104 | Header alignment issue              | Minor    | P3       |

5\. Track the defect lifecycle:

```
NEW
  ↓
ASSIGNED
  ↓
IN_PROGRESS
  ↓
RESOLVED
  ↓
VERIFIED
  ↓
CLOSED
```
