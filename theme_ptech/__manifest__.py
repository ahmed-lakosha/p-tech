# -*- encoding: utf-8 -*-
{
    'name': "Ptech theme",
    'summary': """
    Modern, responsive Odoo theme with customization & multilingual support.
    """,
    'description': """
    Optimized for performance, SEO, and seamless Odoo module integration.
    """,
    'author': "ahmed.loakosha94@gmail.com",
    'sequence': 1,
    'contributors': [
        "<Ahmed Lakosha> <<ahmed.loakosha94@gmail.com>>"
    ],
    'category': 'Theme',
    'version': '0.1',
    'depends': ['theme_common', 'website_blog', 'social_media', 'mass_mailing'],
    'data': [
        'security/ir.model.access.csv',

        'views/customize_template.xml',
        'views/website_services.xml',
        'views/website_partners.xml',
        'views/website_blogs.xml',

        'data/pages.xml',
    ],
    'images': [
        'static/description/ptech_description.png',
        'static/description/ptech_screenshot.png',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_ptech/static/src/lib/owl-carousel/css/owl.carousel.min.css',
            'theme_ptech/static/src/lib/owl-carousel/css/owl.theme.default.min.css',
            'theme_ptech/static/src/lib/owl-carousel/js/owl.carousel.min.js',
            'theme_ptech/static/src/lib/bootstrap-icons/bootstrap-icons.css',
            'theme_ptech/static/src/scss/styles.scss',
            'theme_ptech/static/src/scss/custom.scss',
            'theme_ptech/static/src/scss/home_style.scss',
            'theme_ptech/static/src/js/lib-call.js',
            'theme_ptech/static/src/js/script.js',
        ],
        'web._assets_primary_variables': [
            'theme_ptech/static/src/scss/primary_variables.scss',
        ],
    },
    'configurator_snippets': {
        'homepage': ['s_discovery', 's_key_images', 's_striped', 's_showcase', 's_image_title', 's_numbers_charts',
                     's_cta_card', 's_kickoff', 's_title', 's_company_team', 's_image_text_overlap', 's_features',
                     's_freegrid', 's_quotes_carousel', 's_call_to_action', 's_numbers_list', 's_color_blocks_2',
                     's_references', 's_cover', 's_text_image', 's_image_text', 's_three_columns',
                     's_numbers_showcase', 's_masonry_block', 's_faq_list', 's_cta_box', 's_process_steps',
                     's_company_team_basic', 's_images_wall', 's_mockup_image', 's_faq_collapse', 's_framed_intro',
                     's_company_team_shapes', 's_title', 's_parallax', 's_numbers_grid',
                     's_shape_image', 's_product_list', 's_picture'],
    },
    'new_page_templates': {
        'about': {
            'personal': ['s_text_cover', 's_image_text', 's_text_block_h2', 's_numbers', 's_features',
                         's_call_to_action'],
        },
        'team': {
            '5': ['s_text_block_h1', 's_text_block', 's_image_gallery', 's_picture'],
        },
        'landing': {
            '1': ['s_banner', 's_features', 's_masonry_block', 's_call_to_action', 's_references', 's_quotes_carousel'],
            '2': ['s_cover', 's_text_image', 's_text_block_h2', 's_three_columns_landing_1', 's_call_to_action'],
            '3': ['s_text_cover', 's_text_block_h2', 's_three_columns', 's_showcase', 's_color_blocks_2',
                  's_quotes_carousel', 's_call_to_action'],
        },
        'services': {
            '2': ['s_text_cover', 's_image_text', 's_text_image', 's_image_text_2nd', 's_call_to_action'],
        },
    },
    'application': False,
    'license': 'LGPL-3',
}
