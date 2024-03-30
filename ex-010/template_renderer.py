import pystache
import logging

def render_template(template_path, data, output_path):
    """
    Renders a mustache template with the provided data and saves the output to a file.

    Parameters:
    - template_path: Path to the mustache template file.
    - data: A dictionary containing the data to be rendered in the template.
    - output_path: Path where the rendered output should be saved.
    """
    try:
        # Load the mustache template
        with open(template_path, 'r') as file:
            template = file.read()

        # Render the template with the provided data
        rendered_content = pystache.render(template, data)

        # Save the rendered content to the specified output path
        with open(output_path, 'w') as file:
            file.write(rendered_content)

        logging.info(f"Template rendered and saved to {output_path}")

    except Exception as e:
        logging.error(f"Error rendering template: {e}")

def render_output_page(entities_info, template_file='entity_template.mustache', output_html='output.html'):
    """
    Prepares data and calls render_template to generate the output HTML file.

    Parameters:
    - entities_info: Dictionary containing entities and their information.
    - template_file: Path to the mustache template file.
    - output_html: The output HTML file name.
    """
    # Prepare the data for rendering
    data = {
        'entities': []
    }
    for entity, info in entities_info.items():
        data['entities'].append({
            'name': entity,
            'summary': info['summary'],
            'details': ', '.join(info['details'])
        })

    # Render the template with the prepared data
    render_template(template_file, data, output_html)
