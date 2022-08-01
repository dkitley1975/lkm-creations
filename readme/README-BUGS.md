[![David's GitHub Banner](/readme/assets/logo/GitHubHeader.png)](https://www.linkedin.com/in/david-kitley-mcnamara)

## LKM-Creations <!-- omit in toc -->

[![LKM Creations](/readme/assets/site-screenshots/lkm-creations-mockup.png)](https://www.linkedin.com/in/david-kitley-mcnamara)
This documentation gives an explanation of the code errors, issues and bugs found during the creation and testing of the site.
Which either remain unresolved or took a long time to resolve.

# Table Of Contents

- [Table Of Contents](#table-of-contents)
  - [Site Info - delivery price and threshold filter](#site-info---delivery-price-and-threshold-filter)
  - [Running migrations to the remote database](#running-migrations-to-the-remote-database)
  - [No metadata found](#no-metadata-found)
  - [image URLs](#image-urls)
  - [Unit tests](#unit-tests)
  - [Pillow](#pillow)
  - [Emails Stopped working initiated by webhooks.](#emails-stopped-working-initiated-by-webhooks)
  - [Images not being displayed on older versions of Safari.](#images-not-being-displayed-on-older-versions-of-safari)
  - [Issue connecting Facebook account to LKM Creations Account (#60)](#issue-connecting-facebook-account-to-lkm-creations-account-60)

## Site Info - delivery price and threshold filter

The site uses a 'Free Delivery Threshold' which is used to determine if a user can get free delivery.
It also has a default delivery charge which is used if the user does not have a free delivery threshold.
The client wanted to be able to alter these values, but the client did not want to alter the code.
So the client created a modal that allows the user to alter these values.
Along with adding other Information the client wanted to add to the site.
However this would allow multiple records to be added to the table.
So to always pull the most recent active record, the below code was created.
At first This worked fine. But when the database was deleted and recreated, migrations had a error saying that the SiteInfo table didn't exist.
Short term solution was to comment out the code, run ``./manage.py makemigrations``, and then run ``./manage.py migrate``.
Load the fixtures for the SiteInfo table. Uncomment the code and then load the remaining fixtures.

```python
free_delivery_threshold = (
    SiteInfo.objects.all()
    .filter(is_active=True)
    .order_by("-created_at")[0]
    .free_delivery_over
    )
    return free_delivery_threshold

default_delivery_price = (
    SiteInfo.objects.all()
    .filter(is_active=True)
    .order_by("-created_at")[0]
    .delivery_price
    )
    return default_delivery_price
```

My long term solution has been to refactor the code to use a function utilizing a try/except block.
The two functions will return the values of the free delivery threshold and default deliver price if it exists. otherwise it will return a default value.

```python
def default_delivery_price():
    try:
        default_delivery_price = (
            SiteInfo.objects.all()
            .filter(is_active=True)
            .order_by("-created_at")[0]
            .delivery_price
            )
        return default_delivery_price
    except:
        return "10"

default_delivery_price = default_delivery_price()


def free_delivery_threshold():
    try:
        free_delivery_threshold = (
            SiteInfo.objects.all()
            .filter(is_active=True)
            .order_by("-created_at")[0]
            .free_delivery_over
            )
        return free_delivery_threshold

    except:
        return "0"

free_delivery_threshold = free_delivery_threshold()
```

This has stopped the need to be commenting out the code before running ``./manage.py makemigrations`` and ``./manage.py migrate``.
Although This may not be the best solution, it has been the best solution I have found so far.

The original filters were also responsible for the unit tests stopping working. At the time I was unaware of this, and didn't connect the filters to the unit tests issues.

## Running migrations to the remote database

Migrations stopped working on the remote database, although worked locally.
Setting were checked and password copied again to the environment, but migrations still failed when being applied to the remote server.
and gave an error, This indicated that psycopg2 was an issue.
psycopg was uninstalled from the environment and ensured it was not installed locally.
The attempt to reinstall failed.
I installed a postgreSQL server and then ran

```bash
PATH=$PATH:/Library/PostgreSQL/12/bin/ pip install psycopg2
```

and tried

```bash
pip3 install psycopg2
```

and the binary version of psycopg2 was installed.
The error still persists and I have not been able to resolve it.
The issue I believe is that I am using a 14 year old Mac, and to install and run correctly the mac need to install X-code which is not able to be installed any longer on my machine.
If the project is opened in gitpod I am able to makemigrations and migrate without the issues appearing to confirm it is definitely a problem on the local machine


## No metadata found

WARNING: No metadata found in ./venv/lib/python3.9/site-packages
Whilst running pip3 freeze --local > requirements.txt

Ran
pip install pip-upgrader. —  pip-upgrade and updated the requirements (allbar django)
this didn’t solve the issue.
Deleted my virtual environment and recreated the virtual enviroment and reinstalled all the packages.
This solved the issue.

## image URLs
Image url didn’t include media/ on the home page.  This was because The image used on the homepage is a reference from the siteadmin app using a custom context passing the data in as a dictionary. This was solved by instead of having just {{ site_info.image }}
I had to add .url to the end like so: {{ site_info.image.url }

## Unit tests
I encountered this error when trying to run unittests:
django.core.exceptions.improperlyconfigured: requested setting installed_apps, but settings are not configured. you must either define the environment variable django_settings_module or call settings.configure() before accessing settings

Solutions tried
I tried adding this line: set DJANGO_SETTINGS_MODULE=mysite.settings to  venv/bin/activate

Checking out previous commits,
Removing my virtual environment and recreating,
Uninstalling Python on my local machine and reinstalling,
Uninstalling all previously install python packages installed locally,
Recreating the project and apps,

My solution was to create a back up locally, delete the repository.
I recreated the project, and apps. I added the models from my local backup and test data.
I added my tests from my local backup.
In conclusion, I don’t know what caused the issue, I know VSCode updated and the python extension updated to the pre-release just prior to the error.
But I recreated the work from my locally stored backed up code, using the same version of VSCode,

## Pillow
After adding the image field in the models for the media, I received this error in the terminal when attempting to apply migrations.

inventory.Media.image_url: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".

Solution uninstall Pillow  9.1 and install Pillow 9.0.1

## Emails Stopped working initiated by webhooks.
I had webhooks installed and running emails were working. After progressing through testing an order went through, I later noticed that emails were no longer being received.
I tried replacing the webhooks with older known working versions of the file, and the emails were still not working.
I took a branch from a known working version and tried running this version and the problem was still there.
This was the first time I had encountered this issue and took several days trying different things.
Eventually I tried the student support and we worked our way through the problem.
We found the issue was not with the webhooks, but with the emails, an additional blank line had been added to the email subject header file.Removing this line fixed the issue.

## Images not being displayed on older versions of Safari.
After updating the site images to webp, I was unable to display the images on older versions of Safari.
After checking additional browser it is confirmed it was because the browser doesn't support webp.
I tried using the latest version of Safari and it worked.
I have instead used this

```HTML
<picture>
        <source srcset="{{ product.image_preferred.url }}"
            type="image/webp">
        <source srcset="{{ product.image.url }}" type="image/jpeg">
        <img src="{{ product.image.url }}"
            alt="{{ product.image_alt_text }}" class="img-fluid mx-auto d-block
            oncontextmenu="return false;">
</picture>
```
This will only use the webp format if the browser supports it. falling back to the jpeg format.
However I have not been able to find a solution to an issue if the image is not on the system and having it display a default image.

To support this I have created functions to convert the supplied images uploaded to webp format, jpeg as a fallback.
The png function is used for the homepage image.

```python
def Convert2jpg(self, saveName):
    """
    Convert the image to a jpg file.
    """
    Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
    convert2jpg_filename = (
        "%s.jpg" % f'"lkm-creations_"{saveName}"_"{str(Current_Date)}'
    )  # create a filename
    convert2jpg_image = Image.open(self.image)
    if convert2jpg_image.mode in ("RGBA", "LA"):
        background = Image.new(
            convert2jpg_image.mode[:-1], convert2jpg_image.size, "#fff"
        )
        background.paste(convert2jpg_image, convert2jpg_image.split()[-1])
        convert2jpg_image = background
    convert2jpg_image.thumbnail((800, 800))
    convert2jpg_image_io = BytesIO()
    convert2jpg_image.save(
        convert2jpg_image_io, format="JPEG", quality=100
    )
    self.image.save(
        convert2jpg_filename,
        ContentFile(convert2jpg_image_io.getvalue()),
        save=False,
    )


def Convert2webp(self, saveName):
    """
    Convert the image to webp format and save it to the database.
    """
    Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
    convert2webp_filename = (
        "%s.webp" % f'"lkm-creations_"{saveName}"_"{str(Current_Date)}'
    )
    convert2webp_image = Image.open(self.image)
    convert2webp_image.thumbnail((800, 800))
    convert2webp_image_io = BytesIO()
    convert2webp_image.save(
        convert2webp_image_io, format="WEBP", quality=90
    )
    self.image_preferred.save(
        convert2webp_filename,
        ContentFile(convert2webp_image_io.getvalue()),
        save=False,
    )


def Convert2png(self, saveName):
    """
    Convert the image to a png file.
    """
    Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
    convert2png_filename = (
        "%s.png" % f'"lkm-creations_"{saveName}"_"{str(Current_Date)}'
    )  # create a filename
    convert2png_image = Image.open(self.image)
    convert2png_image.thumbnail((900, 600))
    convert2png_image_io = BytesIO()
    convert2png_image.save(convert2png_image_io, format="PNG", quality=100)
    self.image.save(
        convert2png_filename,
        ContentFile(convert2png_image_io.getvalue()),
        save=False,
    )
```
These ensure the image is saved in the correct format.

## Issue connecting Facebook account to LKM Creations Account (#60)
Whilst I believe that everything is setup correctly, I was unable to connect my Facebook account to my LKM Creations account.
I think it may be because the facebook account service is not activated correctly, or it is waiting to be activated on confirmation of the URL.
I don't know what the issue is and will have to remove the service for project submission.
