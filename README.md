# Creator Fieldnotes

An independent, static educational website about SEO Studio Tools and YouTube SEO. Ten HTML pages use one local stylesheet, a tiny navigation script, and a local SVG favicon. No backend, analytics, external fonts, scripts, or forms are included. The only external website hyperlink is the homepage CTA to SEO Studio Tools. The site is not affiliated with YouTube or SEO Studio Tools.

## Publish with GitHub Actions (recommended)

1. Create a **public** GitHub repository. The default branch should be called `main`. For a user site use `YOUR-USERNAME.github.io`; for a project site choose a name such as `seo-studio-resources`.
2. Extract the ZIP. Upload the **contents** of the `seo-studio-resources` folder to the root of the repository—not the enclosing folder. Include the hidden `.github/workflows/pages.yml` file. GitHub's web uploader may not show hidden folders on every operating system; if needed, reveal hidden files or use Git to upload them.
3. Open your repository **Settings → Pages → Build and deployment** and select **GitHub Actions** as the source. The included workflow runs on pushes to `main` and can also be run manually from the Actions tab. It derives the GitHub Pages address from the repository owner and name, then sets the canonical URLs, Open Graph URLs, sitemap, and robots file in the deployed artifact. It does not modify the files in your repository.
4. Wait for the deployment workflow to finish. Open the URL shown under Settings → Pages or in the workflow deployment. For a project site it is normally `https://YOUR-USERNAME.github.io/REPOSITORY/`; for a user site it is `https://YOUR-USERNAME.github.io/`. Test navigation, including on a phone, and open `sitemap.xml` and `robots.txt` under that exact base path.
5. In Google Search Console add and verify a property for the actual site URL. Open **Sitemaps**, enter `sitemap.xml` for that property, and submit it. Check the status after processing. Submission is a discovery hint, not a guarantee of crawling or indexing.

GitHub Pages availability and visibility depend on your GitHub plan and repository settings. For an organization, an administrator may need to allow Pages or Actions. If the branch is not `main`, change the workflow trigger. For a custom domain, update the workflow to call `python3 configure.py https://your-domain.example/` using your actual address and configure the domain in GitHub Pages; do not use the automatically calculated github.io URL.

## Manual deployment / another static host

Before uploading files, run `python3 configure.py https://YOUR-USERNAME.github.io/REPOSITORY/` from the project directory, substituting your actual public URL and keeping its trailing slash. For a user site, omit the repository segment. This updates all ten pages' canonical and Open Graph URLs and regenerates `sitemap.xml` and `robots.txt`; it can be rerun when the site address changes. Then upload the resulting files and publish the repository branch/folder through GitHub Pages. Python is needed only for configuration; the published website is static.

**Important:** The shipped source contains example placeholders (`YOUR-USERNAME` and `YOUR-REPOSITORY`) because the final address was not supplied. Do not submit its sitemap or publish it via a branch-based deployment without running the configuration step. The Actions deployment configures the deployed artifact automatically.

## Maintenance

- Replace the contact page's unavailable-contact note only after an owner supplies a real public contact method. No contact form is functional or implied.
- Review YouTube policies and monetization requirements periodically; eligibility, country coverage and features can change.
- Internal links are relative and work within a GitHub Pages repository subdirectory. Sitemap and canonical URLs are absolute after configuration. A canonical is a hint, not a guarantee that Google will index or choose a particular URL.
- The FAQ sections use native HTML `details` and work without JavaScript. Navigation stays visible on small screens when JavaScript is unavailable.
