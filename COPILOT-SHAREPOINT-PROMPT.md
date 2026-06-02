# Copilot Prompt: Cloud Readiness Accelerator SharePoint Publishing
## Detailed Instructions for Microsoft Copilot

---

## 📋 Context

I need to publish the **Cloud Readiness Accelerator Framework** to SharePoint at:
**https://raxglobal.sharepoint.com/sites/pcproservind/SitePages/**

This is an enterprise cloud readiness assessment framework with:
- 24+ reusable templates
- 12+ integration guides
- 8+ customization guides
- Real-world case studies
- Complete methodology documentation

---

## 🎯 Task Overview

**Objective**: Create a comprehensive SharePoint site structure and publish all framework content

**Timeline**: 6 days (May 2-7, 2026)
**Go-Live**: May 8, 2026
**Team Size**: 8 people
**Total Effort**: 40 hours

---

## 📁 Source Files Location

All source files are located in: `C:\Users\upen9003\OneDrive - Rackspace Inc\Projects\DMG\Cloud Readiness acceleartor\`

**Key Files**:
- `SHAREPOINT-PAGE-CONTENT.md` - Main landing page content
- `SHAREPOINT-PAGE.html` - HTML version of landing page
- `SHAREPOINT-IMPLEMENTATION-PLAN.md` - Detailed 6-day timeline
- `SHAREPOINT-DEPLOYMENT-GUIDE.md` - Step-by-step deployment guide
- All 24+ templates in `Templates/` folder
- All guides in `Integration-Guides/` and `Customization-Guides/` folders
- Case studies and resources

---

## 🚀 Day 1: Site Preparation (May 2)

### Task 1.1: Create SharePoint Site Structure

**What to do**:
1. Navigate to: https://raxglobal.sharepoint.com/sites/pcproservind/
2. Go to **Shared Documents**
3. Create the following folder structure:
   ```
   Shared Documents/
   ├── Framework-Overview/
   ├── Templates/
   │   ├── Discovery-Templates/
   │   ├── Scoring-Templates/
   │   ├── Business-Case-Templates/
   │   ├── Risk-Compliance-Templates/
   │   ├── Governance-Templates/
   │   └── Reporting-Templates/
   ├── Guides/
   │   ├── Phase-Guides/
   │   ├── Integration-Guides/
   │   ├── Customization-Guides/
   │   └── Quality-Assurance/
   ├── Case-Studies/
   └── Resources/
   ```

**Copilot Instructions**:
```
Create a detailed step-by-step guide for creating this folder structure in SharePoint Online. 
Include:
1. Screenshots or descriptions of where to click
2. Exact folder names to use
3. Verification steps to confirm folders are created
4. How to set folder permissions
5. Best practices for folder organization
```

---

### Task 1.2: Create Main Landing Page

**What to do**:
1. Go to **SitePages**
2. Click **+ New** → **Page**
3. Name it: **Cloud-Readiness-Accelerator**
4. Add the following web parts:
   - Hero banner with title and subtitle
   - Quick Links section (6 links)
   - Overview section
   - Statistics section (8 stat boxes)
   - Call-to-action buttons

**Page Content Source**: `SHAREPOINT-PAGE-CONTENT.md`

**Copilot Instructions**:
```
I need to create a professional SharePoint landing page for the Cloud Readiness Accelerator Framework.

Page Details:
- Title: "Cloud Readiness Accelerator Framework"
- Subtitle: "Enterprise Cloud Migration Assessment & Planning Platform"
- URL: https://raxglobal.sharepoint.com/sites/pcproservind/SitePages/Cloud-Readiness-Accelerator.aspx

Required Web Parts:
1. Hero Banner - with gradient background (blue to green)
2. Quick Links - 6 links to: Getting Started, Templates, Guides, Case Studies, FAQ, Support
3. Overview Section - with framework description
4. Statistics - 8 stat boxes showing: 20 Requirements, 12 Components, 24+ Templates, 4 Phases, 5 Dimensions, 3 Hyperscalers, 8 Guides, 100% Reusable
5. Features Section - bullet list of core capabilities
6. Call-to-Action Buttons - Download Framework, Getting Started

Provide:
1. Step-by-step instructions for creating each web part
2. Exact text to use for each section
3. Formatting and styling recommendations
4. How to add links and buttons
5. How to save and publish the page
```

---

### Task 1.3: Configure Site Navigation

**What to do**:
1. Set up site navigation menu
2. Add links to main pages
3. Add links to document library
4. Configure breadcrumb navigation

**Copilot Instructions**:
```
Help me configure SharePoint site navigation for the Cloud Readiness Accelerator site.

Current Site: https://raxglobal.sharepoint.com/sites/pcproservind/

Navigation Structure Needed:
- Home
- Cloud Readiness Accelerator (main landing page)
  - Getting Started
  - Templates
  - Guides
  - Case Studies
  - FAQ
  - Support
- Shared Documents
  - Framework-Overview
  - Templates
  - Guides
  - Case-Studies
  - Resources

Provide:
1. How to access site navigation settings
2. Step-by-step instructions to add navigation links
3. How to organize links hierarchically
4. How to set up breadcrumb navigation
5. How to test navigation
```

---

### Task 1.4: Set Up Permissions

**What to do**:
1. Create Azure AD security groups
2. Assign permissions to groups
3. Configure sharing settings

**Copilot Instructions**:
```
Help me set up permissions for the Cloud Readiness Accelerator SharePoint site.

Required Security Groups:
1. Cloud-Readiness-Accelerator-Owners
   - Permission Level: Full Control
   - Members: Cloud Solutions Architecture Team

2. Cloud-Readiness-Accelerator-Users
   - Permission Level: Edit
   - Members: Authorized consultants and architects

3. Cloud-Readiness-Accelerator-Stakeholders
   - Permission Level: Read
   - Members: Stakeholders and read-only users

Provide:
1. How to create Azure AD security groups
2. How to assign groups to SharePoint site
3. How to set permission levels for each group
4. How to configure sharing settings
5. How to verify permissions are working correctly
```

---

## 📥 Day 2: Document Upload (May 3)

### Task 2.1: Upload Core Documentation

**What to do**:
Upload the following files to `Framework-Overview/` folder:
- FRAMEWORK-INDEX.md
- QUICK-START-GUIDE.md
- Methodology-Overview.md
- EXECUTIVE-SUMMARY.md
- EXECUTIVE-ACTION-SUMMARY.md
- DEPLOYMENT-STRATEGY.md

**Copilot Instructions**:
```
Help me upload documents to SharePoint and add metadata.

Documents to Upload:
Location: C:\Users\upen9003\OneDrive - Rackspace Inc\Projects\DMG\Cloud Readiness acceleartor\

Files:
1. FRAMEWORK-INDEX.md
2. QUICK-START-GUIDE.md
3. Methodology-Overview.md
4. EXECUTIVE-SUMMARY.md
5. EXECUTIVE-ACTION-SUMMARY.md
6. DEPLOYMENT-STRATEGY.md

Destination: https://raxglobal.sharepoint.com/sites/pcproservind/Shared Documents/Framework-Overview/

For Each File, Add Metadata:
- Title: [Descriptive title]
- Description: [Brief description]
- Tags: cloud, assessment, framework, readiness

Provide:
1. Step-by-step upload instructions
2. How to add metadata to documents
3. How to organize documents in folders
4. How to set document permissions
5. How to verify uploads are complete
```

---

### Task 2.2: Upload Templates

**What to do**:
Upload all 24+ templates to appropriate subfolders in `Templates/` folder

**Template Organization**:
```
Templates/
├── Discovery-Templates/
│   ├── Application-Discovery-Profiling-Template.md
│   ├── Infrastructure-Profiling-Template.md
│   └── Dependency-Mapping-Template.md
├── Scoring-Templates/
│   ├── Cloud-Readiness-Scoring-Template.md
│   ├── AWS-Evaluation-Template.md
│   ├── Azure-Evaluation-Template.md
│   ├── GCP-Evaluation-Template.md
│   └── Hyperscaler-Decision-Matrix-Template.md
├── Business-Case-Templates/
│   ├── Business-Case-Template.md
│   └── TCO-ROI-Analysis-Template.md
├── Risk-Compliance-Templates/
│   ├── Risk-Assessment-Template.md
│   └── Compliance-Assessment-Template.md
├── Governance-Templates/
│   └── Governance-Model-Template.md
└── Reporting-Templates/
    ├── Executive-Summary-Report-Template.md
    ├── Detailed-Assessment-Report-Template.md
    └── Migration-Roadmap-Template.md
```

**Copilot Instructions**:
```
Help me upload 24+ templates to SharePoint in organized subfolders.

Source Location: C:\Users\upen9003\OneDrive - Rackspace Inc\Projects\DMG\Cloud Readiness acceleartor\Templates\

Destination: https://raxglobal.sharepoint.com/sites/pcproservind/Shared Documents/Templates/

Template Categories:
1. Discovery Templates (3 files)
2. Scoring Templates (5 files)
3. Business Case Templates (2 files)
4. Risk & Compliance Templates (2 files)
5. Governance Templates (1 file)
6. Reporting Templates (3 files)

For Each Template:
- Upload to appropriate subfolder
- Add metadata (Title, Description, Tags)
- Set permissions
- Add usage instructions in description

Provide:
1. Bulk upload instructions
2. How to organize files in subfolders
3. How to add consistent metadata
4. How to create a template index
5. How to make templates easily discoverable
```

---

### Task 2.3: Upload Guides

**What to do**:
Upload all guides to appropriate subfolders in `Guides/` folder

**Copilot Instructions**:
```
Help me upload guides to SharePoint.

Source Location: C:\Users\upen9003\OneDrive - Rackspace Inc\Projects\DMG\Cloud Readiness acceleartor\

Guides to Upload:
1. Phase Guides (4 files):
   - Discovery-Phase-Guide.md
   - Analysis-Phase-Guide.md
   - Evaluation-Phase-Guide.md
   - Planning-Phase-Guide.md

2. Integration Guides (3 files):
   - CMDB-Integration-Guide.md
   - Monitoring-Tool-Integration-Guide.md
   - Cloud-Assessment-Tool-Integration-Guide.md

3. Customization Guides (2 files):
   - Industry-Customization-Guide.md
   - Organization-Size-Adaptation-Guide.md

4. Quality Assurance (1 file):
   - Data-Validation-Checklist.md

Destination: https://raxglobal.sharepoint.com/sites/pcproservind/Shared Documents/Guides/

Provide:
1. Upload instructions for each category
2. How to organize guides by type
3. How to add descriptions and tags
4. How to create a guides index
5. How to link guides from main pages
```

---

### Task 2.4: Upload Case Studies & Resources

**What to do**:
Upload case studies and resources

**Copilot Instructions**:
```
Help me upload case studies and resources to SharePoint.

Case Studies (4 files):
- DMG-Media-UK-Application-Inventory.md
- DMG-Media-UK-Readiness-Assessment.md
- DMG-Media-UK-Business-Case.md
- DMG-Media-UK-Migration-Roadmap.md

Resources (3 files):
- Industry-Benchmarks.md
- Cloud-Service-Comparisons.md
- Glossary-and-Terminology.md

Destination:
- Case Studies: https://raxglobal.sharepoint.com/sites/pcproservind/Shared Documents/Case-Studies/
- Resources: https://raxglobal.sharepoint.com/sites/pcproservind/Shared Documents/Resources/

Provide:
1. Upload instructions
2. How to organize case studies
3. How to add descriptions
4. How to make resources easily searchable
5. How to link resources from main pages
```

---

## 📄 Day 3: Navigation & Lists (May 4)

### Task 3.1: Create Supporting Pages

**What to do**:
Create 6 supporting pages with specific content

**Copilot Instructions**:
```
Help me create 6 supporting SharePoint pages for the Cloud Readiness Accelerator site.

Pages to Create:
1. Getting-Started.aspx
   - Overview of framework
   - 5-minute introduction
   - Quick-start steps
   - Links to guides

2. Templates.aspx
   - List of all templates
   - Brief descriptions
   - Download links
   - Usage instructions

3. Guides.aspx
   - Phase-specific guides
   - Integration guides
   - Customization guides
   - Best practices

4. Case-Studies.aspx
   - DMG Media UK reference
   - Assessment results
   - Business case outcomes
   - Lessons learned

5. FAQ.aspx
   - Common questions
   - Answers and guidance
   - Links to resources
   - Contact information

6. Support.aspx
   - Support channels
   - Contact information
   - Office hours
   - Feedback form

For Each Page:
- Create page with appropriate title
- Add content sections
- Add links to relevant documents
- Add call-to-action buttons
- Format professionally

Provide:
1. Step-by-step instructions for creating each page
2. Exact content for each page
3. How to add links and buttons
4. How to format pages professionally
5. How to save and publish pages
```

---

### Task 3.2: Create Lists & Forms

**What to do**:
Create announcements list, feedback form, and project registry

**Copilot Instructions**:
```
Help me create SharePoint lists and forms.

1. Announcements List: "Framework-Updates"
   Columns:
   - Title
   - Body
   - Category (Release, Update, Announcement)
   - Date
   
   Initial Announcement:
   - Title: "Cloud Readiness Accelerator v1.0 Released"
   - Body: "Framework is now available for use"
   - Category: Release
   - Date: May 8, 2026

2. Feedback Form: "Cloud Readiness Accelerator Feedback"
   Questions:
   - Which templates did you use? (Text)
   - How helpful was the framework? (1-5 scale)
   - What improvements would you suggest? (Text)
   - Would you recommend this framework? (Yes/No)
   - Your name and email (Text)

3. Project Registry List: "Project-Registry"
   Columns:
   - Project Name
   - Organization
   - Assessment Date
   - Hyperscaler Selected
   - Business Case ROI
   - Status (In Progress, Completed, Planned)
   - Team Lead
   - Contact Email

Provide:
1. How to create each list
2. How to add columns and configure field types
3. How to create the feedback form
4. How to link form to list
5. How to configure notifications
```

---

## ⚙️ Day 4: Configuration & Testing (May 5)

### Task 4.1: Configure Permissions & Alerts

**Copilot Instructions**:
```
Help me configure permissions and alerts for the SharePoint site.

Permissions Configuration:
1. Verify security groups are assigned correctly
2. Test access for each permission level
3. Configure sharing settings
4. Enable external sharing (if applicable)

Alerts Configuration:
1. Create alert for document updates
2. Create alert for new announcements
3. Create alert for feedback submissions
4. Configure email notifications

Provide:
1. How to verify permissions are working
2. How to test access for different roles
3. How to set up alerts
4. How to configure email notifications
5. How to troubleshoot permission issues
```

---

### Task 4.2: Comprehensive Testing

**Copilot Instructions**:
```
Help me create a comprehensive testing checklist for the SharePoint site.

Functional Testing:
- [ ] All pages load correctly
- [ ] Navigation works properly
- [ ] Links are functional
- [ ] Documents download correctly
- [ ] Forms submit successfully
- [ ] Lists display correctly
- [ ] Permissions work as expected
- [ ] Search functionality works

User Experience Testing:
- [ ] Page layout is clear
- [ ] Content is easy to find
- [ ] Instructions are clear
- [ ] Mobile view works
- [ ] Performance is acceptable

Security Testing:
- [ ] Permissions are enforced
- [ ] Unauthorized access is blocked
- [ ] Data is encrypted
- [ ] Audit logging works

Provide:
1. Detailed testing procedures
2. How to document test results
3. How to identify and log issues
4. How to prioritize issues
5. How to verify fixes
```

---

## 🎓 Day 5: Training & Promotion (May 6)

### Task 5.1: Create Training Materials

**Copilot Instructions**:
```
Help me create training materials for the Cloud Readiness Accelerator SharePoint site.

Training Materials Needed:
1. Tutorial Videos (scripts):
   - How to access the framework
   - How to use the templates
   - How to customize for your organization
   - How to integrate with systems

2. Quick Reference Guides:
   - Getting started guide
   - Template usage guide
   - Integration guide
   - Customization guide

3. FAQ Document:
   - Common questions
   - Answers and guidance
   - Links to resources

Provide:
1. Scripts for tutorial videos
2. Outline for quick reference guides
3. FAQ content
4. How to record and upload videos
5. How to distribute training materials
```

---

### Task 5.2: Prepare Launch Announcement

**Copilot Instructions**:
```
Help me create a launch announcement for the Cloud Readiness Accelerator framework.

Announcement Details:
- Target Audience: All team members
- Delivery Method: Email
- Date: May 8, 2026
- Time: 9:00 AM

Announcement Should Include:
1. Framework overview (2-3 sentences)
2. Key benefits (3-4 bullet points)
3. SharePoint site link
4. Quick-start guide link
5. Contact information
6. Invitation to provide feedback

Provide:
1. Complete announcement text
2. Email subject line
3. Formatting recommendations
4. Distribution list
5. Follow-up communication plan
```

---

### Task 5.3: Set Up Support Channel

**Copilot Instructions**:
```
Help me set up a Microsoft Teams channel for support.

Channel Details:
- Channel Name: Cloud-Readiness-Accelerator
- Channel Description: Support and discussion for the Cloud Readiness Accelerator framework
- Channel Type: Standard

Channel Setup:
1. Create channel
2. Add channel description
3. Pin important resources
4. Assign support team members
5. Configure notifications

Provide:
1. Step-by-step channel creation instructions
2. How to add members
3. How to pin resources
4. How to configure notifications
5. How to set up channel guidelines
```

---

## 🚀 Day 6: Launch Preparation (May 7)

### Task 6.1: Final Testing & Review

**Copilot Instructions**:
```
Help me create a final pre-launch checklist.

Pre-Launch Checklist:
- [ ] All pages are live and accessible
- [ ] All documents are uploaded and organized
- [ ] All links are functional
- [ ] Permissions are configured correctly
- [ ] Lists and forms are working
- [ ] Alerts and notifications are configured
- [ ] Training materials are ready
- [ ] Support team is trained
- [ ] Launch announcement is ready
- [ ] Support channel is set up

For Each Item:
- Verify it's complete
- Document any issues
- Create action items for issues
- Get stakeholder sign-off

Provide:
1. Detailed checklist
2. How to verify each item
3. How to document issues
4. How to prioritize issues
5. How to get sign-off
```

---

### Task 6.2: Publish All Pages

**Copilot Instructions**:
```
Help me publish all SharePoint pages.

Pages to Publish:
1. Cloud-Readiness-Accelerator.aspx (main landing page)
2. Getting-Started.aspx
3. Templates.aspx
4. Guides.aspx
5. Case-Studies.aspx
6. FAQ.aspx
7. Support.aspx

For Each Page:
1. Review content
2. Verify all links work
3. Check formatting
4. Publish page
5. Verify page is live

Provide:
1. How to publish pages
2. How to verify pages are live
3. How to test all links
4. How to check formatting
5. How to troubleshoot publishing issues
```

---

## 📊 Success Criteria

### Launch Day (May 8)
- ✅ All pages live and accessible
- ✅ All documents available for download
- ✅ All links functional
- ✅ Support team ready
- ✅ Launch event held successfully

### Week 1 (May 8-14)
- ✅ 50+ unique users access site
- ✅ 10+ templates downloaded
- ✅ 5+ feedback submissions
- ✅ 0 critical issues
- ✅ Support team responds to all questions

### Month 1 (May 8 - June 8)
- ✅ 200+ unique users access site
- ✅ 50+ templates downloaded
- ✅ 3+ projects using framework
- ✅ 20+ feedback submissions
- ✅ Framework improvements planned

---

## 📞 Support & Contact

### During Implementation
- **Project Lead**: Cloud Solutions Architecture Team
- **Email**: cloud-readiness@rackspace.com
- **Teams**: Cloud-Readiness-Accelerator

### After Launch
- **Email**: cloud-readiness@rackspace.com
- **Teams**: Cloud-Readiness-Accelerator
- **Office Hours**: Tuesdays 2:00 PM

---

## 🎯 Next Steps

1. **Review this prompt** with your SharePoint administrator
2. **Start Day 1 tasks** immediately
3. **Follow the 6-day timeline**
4. **Execute each task** as outlined
5. **Test thoroughly** before launch
6. **Go live on May 8**

---

**Status**: ✅ Ready for Copilot Implementation
**Timeline**: 6 days (May 2-7, 2026)
**Go-Live**: May 8, 2026
**Effort**: 40 hours
**Team**: 8 people

**Let's Deploy! 🚀**
