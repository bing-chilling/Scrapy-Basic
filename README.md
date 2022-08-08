# Scrapy-Basic
<p><em>In this scraping project, the site 'https://quotes.toscrape.com/' was scarped. The following actions were performed : </p></em>
<ul><em>
  <li>We logged into the site by extracting the csrf token</li>
  <li>We scraped the following data:
    <ol>
      <li>Quotes</li>
      <li>Author</li>
      <li>Tags</li>
   </ol>
  </li>
  <li>We filtered some of the quotes using regex to remove some unicode.</li>
  <li>We etracted the data into the json file named 'quotes'.</li>
</ul></em>
<hr>
<p><b>Keep in mind the sites used <em>did not</em> load in data dynamically and the data parsed was <em>not stored</em> into any database ( sql / nosql )</p></b>
