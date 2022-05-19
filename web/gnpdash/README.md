<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/wifredgithuka/gnpdash">
    <img src="https://avic-storage.ap-south-1.linodeobjects.com/gnp_logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">GNP Dashboard</h3>

  <p align="center">
    A Browser Based Digital Vehicle Dashboard [Nissan Note E11] Running Off the CAN Bus 
    <br />
    <a href="https://gnp.githuka.com"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/wifredgithuka/gnpdash">View Demo Online[Youtube]</a>
    ·
    <a href="https://github.com/wifredgithuka/gnpdash/issues">Report Issues To Developer</a>
    ·
    <a href="https://github.com/wifredgithuka/gnpdash/feature">Request Something New</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The GNP Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot](https://avic-storage.ap-south-1.linodeobjects.com/gnp_dash.png)

The GNP Dash project is a project that shows realtime CAN Messages and mimics the movement of vehicle dashboard components like:

* Speedomenter
* Tachomenter
* Indicators
* Lapms
* Engine status etc

All the information is displayed via a web broswer with JSON packets for sending the data. The response might be abit slower than
the vehicle's dashboard readout due to the preprocessing required. The vehicle's CAN Bus is a high speed interface for linking all
devices in a network to communicate with each other, therefore reducing wires and unessesary complexity.

This project is an upgrade of Luke Mercy's work who started this project about a year ago. I have ported the work to Nissan and the
progress has been gradual despite slow due to some challenges along the way.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This project is simple. Bootstrao HTML Frontend and Django Backend. The rest of the tools and for support.

* [Django](https://www.djangoproject.com/)
* [Python](https://www.python.org/)
* [CAN Bus](https://www.csselectronics.com/pages/can-bus-simple-intro-tutorial)
* [React.js](https://reactjs.org/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

Am really wondering what to write for this section despite the fact that I wrote it. Anyway you shall need a computer with
a browser. Clone the repo, get into requirements.txt and fly away. 

### Prerequisites

..Working on this...


<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [ ] Add Nissan Note E11 DBC File
- [x] Backup Project
- [x] Add "components" document to easily copy & paste sections of the readme
- [x] Multi-language Support
    - [x] Chinese

See the [open issues](https://github.com/wilfredgithuka/gnpdash/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/gnpdash`)
3. Commit your Changes (`git commit -m 'Add some changes`)
4. Push to the Branch (`git push origin`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@wilfredgithuka](https://twitter.com/wilfredgithuka) - dev@githuka.com.com

Project Link: [https://github.com/wilfredgithuka/gnpdash](https://github.com/wilfredgithuka/gnpdash)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
